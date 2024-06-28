from manim import *


class RTOutputID(Scene):

    def construct(self):

        # title
        text_title = Text(
            "Target ID Output", font_size=36.0, color=WHITE, stroke_width=0
        ).to_edge(UP, buff=0.5)
        self.add(text_title)

        lane_width = 0.9
        half_lane_width = 0.45

        # add lines
        line_num = 6
        for i in range(line_num):
            if i == 0 or i == 5:
                line = Line(LEFT * 8, RIGHT * 8, stroke_width=5)
            else:
                line = DashedLine(
                    LEFT * 8,
                    RIGHT * 8,
                    dash_length=0.6,
                    dashed_ratio=0.5,
                    stroke_width=3,
                )
            line.shift(UP * (2.5 - i) * lane_width)
            self.add(line)

        # add text of lane name
        lane_name = (
            "host_lane",
            "left_lane",
            "right_lane",
            "n_left_lane",
            "n_right_lane",
        )
        for name in lane_name:
            text = Text(name, font_size=18.0, color=WHITE, stroke_width=0)
            text.to_edge(LEFT, buff=0.1)
            text.shift(UP * (2 - lane_name.index(name)) * lane_width)
            self.add(text)

        # add ego
        ego_length = 1.25
        ego_width = 0.5
        ego_stroke_width = 2.0
        ego_stroke_opacity = 1.0

        ego = Rectangle(
            height=ego_width,
            width=ego_length,
            color="blue_d",
            stroke_width=ego_stroke_width,
            stroke_opacity=ego_stroke_opacity,
        ).shift(LEFT)
        ego_text = Text("ego", fill_opacity=1.0, stroke_width=0, font_size=24.0).shift(
            LEFT, DOWN * 0.04
        )
        self.add(ego, ego_text)

        # add edge
        edge = DashedLine(
            DOWN * (half_lane_width + 2 * lane_width),
            UP * (half_lane_width + 2 * lane_width),
            color="red_c",
            stroke_width=2.0,
            dash_length=0.15,
            dashed_ratio=0.6,
        ).shift(LEFT * (1.0 - ego_length / 2))
        self.add(edge)

        # add front targets
        front_gargets_num = 8
        front_targets = []
        front_gargets_pos = (
            RIGHT * 1.2,
            RIGHT * 5.0,
            UP * lane_width + RIGHT * 1.5,
            DOWN * lane_width + RIGHT * 2.0,
            UP * lane_width + RIGHT * 4.0,
            DOWN * lane_width + RIGHT * 4.5,
            UP * (2 * lane_width) + RIGHT * 3.5,
            DOWN * (2 * lane_width) + RIGHT * 1.5,
        )
        for i in range(front_gargets_num):
            if i in [0, 1]:
                set_color = "green_b"
            elif i in [2, 3, 4, 5]:
                set_color = "yellow_b"
            else:
                set_color = "purple_b"
            rt = Rectangle(
                height=ego_width,
                width=ego_length,
                color=set_color,
                stroke_width=ego_stroke_width,
                stroke_opacity=ego_stroke_opacity,
            ).shift(front_gargets_pos[i])
            head = Line(
                rt.get_center(),
                rt.get_right(),
                color=rt.get_color(),
                stroke_width=rt.stroke_width - 0.5,
            )
            front_targets.append(rt)
            self.add(rt, head)

        for rt in front_targets:
            if front_targets.index(rt) in [6, 7]:
                rt_name = "RT" + str(front_targets.index(rt) + 6)
            else:
                rt_name = "RT" + str(front_targets.index(rt) + 1)
            set_color = rt.get_color()
            text = Text(
                rt_name,
                color=set_color,
                fill_opacity=1.0,
                stroke_width=0,
                font_size=18.0,
            )
            text.move_to(rt.get_center())
            self.add(text)

        # rear target
        radar_size = 0.07
        radar_stroke_width = 2.5
        radar_stroke_opacity = 1.0
        radar_text_buff = 0.12
        radar_text_font_size = 16.0

        rear_gargets_num = 7
        rear_targets = []
        rear_gargets_pos = (
            LEFT * 3.5,
            UP * lane_width + LEFT * 2.0,
            DOWN * lane_width + LEFT,
            UP * lane_width + LEFT * 3.5,
            DOWN * lane_width + LEFT * 4.0,
            UP * (2 * lane_width) + LEFT * 2.5,
            DOWN * (2 * lane_width) + LEFT * 2.5,
        )
        for i in range(rear_gargets_num):
            if i == 0:
                set_color = "gold_b"
            elif i in [1, 2, 3, 4]:
                set_color = "maroon_b"
            else:
                set_color = "purple_b"
            rt = Circle(
                radius=radar_size,
                color=set_color,
                stroke_width=radar_stroke_width,
                stroke_opacity=radar_stroke_opacity,
            ).shift(rear_gargets_pos[i])
            rear_targets.append(rt)
            self.add(rt)

        for rt in rear_targets:
            if rear_targets.index(rt) in [5, 6]:
                rt_name = "RT" + str(rear_targets.index(rt) + 9)
            else:
                rt_name = "RT" + str(rear_targets.index(rt) + 7)
            set_color = rt.get_color()
            text = Text(
                rt_name,
                color=set_color,
                fill_opacity=1.0,
                stroke_width=0,
                font_size=radar_text_font_size,
            )
            text.next_to(rt, DOWN, buff=radar_text_buff)
            self.add(text)

        # add label
        label_vision = (
            Rectangle(
                height=0.3,
                width=0.75,
                stroke_width=ego_stroke_width,
                stroke_opacity=ego_stroke_opacity,
            )
            .to_edge(DOWN, buff=0.7)
            .to_edge(RIGHT, buff=1.5)
        )
        vision_head = Line(
            label_vision.get_center(),
            label_vision.get_right(),
            color=label_vision.get_color(),
            stroke_width=label_vision.stroke_width - 0.5,
        )
        label_vision_text = Text(
            " : vision",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=18.0,
        ).next_to(label_vision, RIGHT, buff=0.2)
        self.add(label_vision, vision_head, label_vision_text)

        label_radar = Circle(
            radius=radar_size,
            color=WHITE,
            stroke_width=radar_stroke_width,
            stroke_opacity=radar_stroke_opacity,
        ).next_to(label_vision, DOWN, buff=0.2)
        label_radar_text = Text(
            " : radar",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=18.0,
        ).next_to(label_vision_text, DOWN, buff=0.2, aligned_edge=LEFT)
        self.add(label_radar, label_radar_text)
