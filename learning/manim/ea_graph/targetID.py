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
                    LEFT * 8, RIGHT * 8, dash_length=0.6, dashed_ratio=0.5, stroke_width=3)
            line.shift(UP * (2.5-i) * lane_width)
            self.add(line)

        # add text of lane name
        lane_name = ("host_lane", "left_lane", "right_lane",
                     "n_left_lane", "n_right_lane")
        for i in range(len(lane_name)):
            text = Text(lane_name[i], font_size=18.0,
                        color=WHITE, stroke_width=0)
            text.to_edge(LEFT, buff=0.1)
            text.shift(UP * (2-i) * lane_width)
            self.add(text)

        # fill_color="blue_c", fill_opacity=1.0
        ego_length = 1.25
        ego_width = 0.5
        ego_stroke_width = 2.0
        ego_stroke_opacity = 1.0

        radar_length = 0.15
        radar_width = 0.15
        radar_stroke_width = 2.0
        radar_stroke_opacity = 1.0
        radar_text_buff = 0.12
        radar_font_size = 16.0

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
        edge = DashedLine(
            DOWN * (half_lane_width + 2 * lane_width),
            UP * (half_lane_width + 2 * lane_width),
            color="red_c",
            stroke_width=2.0,
            dash_length=0.15,
            dashed_ratio=0.6,
        ).shift(LEFT * (1.0 - ego_length / 2))

        # add front targets
        # front_gargets_num = 8
        # front_targets = []
        # for i in range(front_gargets_num):
        #     if i < 2:
        #         set_color = "green_b"
        #     elif i < 6:
        #         set_color = "yellow_b"
        #     else:
        #         set_color = "purple_b"
        #     rt = Rectangle(height=ego_width, width=ego_length, color=set_color,
        #                    stroke_width=ego_stroke_width, stroke_opacity=ego_stroke_opacity)
        #     front_targets.append(rt)

        rt1 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="green_b",
            stroke_width=ego_stroke_width,
            stroke_opacity=ego_stroke_opacity,
        ).next_to(ego, RIGHT * 3.5)
        rt2 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="green_b",
            stroke_width=ego_stroke_width,
            stroke_opacity=ego_stroke_opacity,
        ).shift(RIGHT * 4.5)
        rt3 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="yellow_b",
            stroke_width=ego_stroke_width,
            stroke_opacity=ego_stroke_opacity,
        ).shift(RIGHT * 1.5, UP * lane_width)
        rt4 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="yellow_b",
            stroke_width=ego_stroke_width,
            stroke_opacity=ego_stroke_opacity,
        ).shift(RIGHT * 1.5, DOWN * lane_width)
        rt5 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="yellow_b",
            stroke_width=ego_stroke_width,
            stroke_opacity=ego_stroke_opacity,
        ).shift(RIGHT * 4.0, UP * lane_width)
        rt6 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="yellow_b",
            stroke_width=ego_stroke_width,
            stroke_opacity=ego_stroke_opacity,
        ).shift(RIGHT * 4.5, DOWN * lane_width)
        rt12 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="purple_b",
            stroke_width=ego_stroke_width,
            stroke_opacity=ego_stroke_opacity,
        ).shift(RIGHT * 2.0, UP * (2 * lane_width))
        rt13 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="purple_b",
            stroke_width=ego_stroke_width,
            stroke_opacity=ego_stroke_opacity,
        ).shift(RIGHT * 1.5, DOWN * (2 * lane_width))

        self.add(rt1, rt2)
        self.add(rt3, rt4)
        self.add(rt5, rt6, rt12, rt13)

        front_targets = [rt1, rt2, rt3, rt4, rt5, rt6, rt12, rt13]
        for i in range(len(front_targets)):
            if i == 6 or i == 7:
                rt_name = "RT" + str(i + 6)
            else:
                rt_name = "RT" + str(i + 1)
            set_color = front_targets[i].get_color()
            text = Text(rt_name, color=set_color, fill_opacity=1.0,
                        stroke_width=0, font_size=18.0)
            text.move_to(front_targets[i].get_center())
            self.add(text)

        # rear target
        rt7 = Rectangle(
            height=radar_length,
            width=radar_width,
            color="gold_b",
            stroke_width=radar_stroke_width,
            stroke_opacity=radar_stroke_opacity,
        ).shift(LEFT * 3.5)
        rt7_text = Text(
            "RT7", color="gold_b", fill_opacity=1.0, stroke_width=0, font_size=radar_font_size
        ).next_to(rt7, DOWN, buff=radar_text_buff)
        rt8 = Rectangle(
            height=radar_length,
            width=radar_width,
            color="maroon_b",
            stroke_width=radar_stroke_width,
            stroke_opacity=radar_stroke_opacity,
        ).shift(LEFT * 2.0, UP * lane_width)
        rt8_text = Text(
            "RT8", color="maroon_b", fill_opacity=1.0, stroke_width=0, font_size=radar_font_size
        ).next_to(rt8, DOWN, buff=radar_text_buff)
        rt9 = Rectangle(
            height=radar_length,
            width=radar_width,
            color="maroon_b",
            stroke_width=radar_stroke_width,
            stroke_opacity=radar_stroke_opacity,
        ).shift(LEFT, DOWN * lane_width)
        rt9_text = Text(
            "RT9", color="maroon_b", fill_opacity=1.0, stroke_width=0, font_size=radar_font_size
        ).next_to(rt9, DOWN, buff=radar_text_buff)
        rt10 = Rectangle(
            height=radar_length,
            width=radar_width,
            color="maroon_b",
            stroke_width=radar_stroke_width,
            stroke_opacity=radar_stroke_opacity,
        ).shift(LEFT * 3.5, UP * lane_width)
        rt10_text = Text(
            "RT10", color="maroon_b", fill_opacity=1.0, stroke_width=0, font_size=radar_font_size
        ).next_to(rt10, DOWN, buff=radar_text_buff)
        rt11 = Rectangle(
            height=radar_length,
            width=radar_width,
            color="maroon_b",
            stroke_width=radar_stroke_width,
            stroke_opacity=radar_stroke_opacity,
        ).shift(LEFT * 4.0, DOWN * lane_width)
        rt11_text = Text(
            "RT11", color="maroon_b", fill_opacity=1.0, stroke_width=0, font_size=radar_font_size
        ).next_to(rt11, DOWN, buff=radar_text_buff)
        rt14 = Rectangle(
            height=radar_length,
            width=radar_width,
            color="purple_b",
            stroke_width=radar_stroke_width,
            stroke_opacity=radar_stroke_opacity,
        ).shift(LEFT * 2.5, UP * (2 * lane_width))
        rt14_text = Text(
            "RT14", color="purple_b", fill_opacity=1.0, stroke_width=0, font_size=radar_font_size
        ).next_to(rt14, DOWN, buff=radar_text_buff)
        rt15 = Rectangle(
            height=radar_length,
            width=radar_width,
            color="purple_b",
            stroke_width=radar_stroke_width,
            stroke_opacity=radar_stroke_opacity,
        ).shift(LEFT * 2.5, DOWN * (2 * lane_width))
        rt15_text = Text(
            "RT15", color="purple_b", fill_opacity=1.0, stroke_width=0, font_size=radar_font_size
        ).next_to(rt15, DOWN, buff=radar_text_buff)
        self.add(ego, ego_text)
        self.add(edge)
        self.add(rt7, rt7_text)
        self.add(rt8, rt9, rt10, rt11, rt8_text,
                 rt9_text, rt10_text, rt11_text)
        self.add(rt14, rt15, rt14_text, rt15_text)
