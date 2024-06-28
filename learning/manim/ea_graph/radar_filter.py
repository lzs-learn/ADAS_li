from manim import *


class RadarFilter(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "background_opacity": 1,
            "frame_height": 32.0,
            "frame_width": 57.0,
        },
    }

    def construct(self):
        #
        lane_width = 0.9
        half_lane_width = 0.45

        left_line = DashedLine(
            LEFT * 8, RIGHT * 8, dash_length=0.6, dashed_ratio=0.5, stroke_width=3
        ).shift(UP * half_lane_width)
        right_line = DashedLine(
            LEFT * 8, RIGHT * 8, dash_length=0.6, dashed_ratio=0.5, stroke_width=3
        ).shift(DOWN * half_lane_width)
        left_left_line = DashedLine(
            LEFT * 8, RIGHT * 8, dash_length=0.6, dashed_ratio=0.5, stroke_width=3
        ).shift(UP * (half_lane_width + lane_width))
        right_right_line = DashedLine(
            LEFT * 8, RIGHT * 8, dash_length=0.6, dashed_ratio=0.5, stroke_width=3
        ).shift(DOWN * (half_lane_width + lane_width))
        left_left_left_line = Line(LEFT * 8, RIGHT * 8, stroke_width=5).shift(
            UP * (half_lane_width + 2 * lane_width)
        )
        right_right_right_line = Line(LEFT * 8, RIGHT * 8, stroke_width=5).shift(
            DOWN * (half_lane_width + 2 * lane_width)
        )
        text_host_lane = Text(
            "host_lane", font_size=18.0, color=WHITE, stroke_width=0
        ).to_edge(LEFT, buff=0.1)
        text_left_lane = (
            Text("left_lane", font_size=18.0, color=WHITE, stroke_width=0)
            .to_edge(LEFT, buff=0.1)
            .shift(UP * lane_width)
        )
        text_right_lane = (
            Text("right_lane", font_size=18.0, color=WHITE, stroke_width=0)
            .to_edge(LEFT, buff=0.1)
            .shift(DOWN * lane_width)
        )
        text_n_left_lane = (
            Text("n_left_lane", font_size=18.0, color=WHITE, stroke_width=0)
            .to_edge(LEFT, buff=0.1)
            .shift(UP * 2 * lane_width)
        )
        text_n_right_lane = (
            Text("n_right_lane", font_size=18.0, color=WHITE, stroke_width=0)
            .to_edge(LEFT, buff=0.1)
            .shift(DOWN * 2 * lane_width)
        )
        self.add(left_line, right_line)
        self.add(left_left_line, right_right_line)
        self.add(left_left_left_line, right_right_right_line)
        # self.add(center_line, left_center_line, right_center_line)
        self.add(
            text_host_lane,
            text_left_lane,
            text_right_lane,
            text_n_left_lane,
            text_n_right_lane,
        )

        # fill_color="blue_c", fill_opacity=1.0
        ego_length = 1.25
        ego_width = 0.5
        ego = Rectangle(
            height=ego_width,
            width=ego_length,
            color="blue_d",
            stroke_width=3.0,
            stroke_opacity=1.0,
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
        rt1 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="green_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(RIGHT * 1.5)
        rt1_text = Text(
            "RT1",
            t2c={"1": "green_b"},
            disable_ligatures=True,
            fill_opacity=1.0,
            stroke_width=0,
            font_size=18.0,
        ).shift(RIGHT * 1.5)
        rt2 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="green_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(RIGHT * 4.5)
        rt2_text = Text(
            "RT2",
            t2c={"2": "green_b"},
            disable_ligatures=True,
            fill_opacity=1.0,
            stroke_width=0,
            font_size=18.0,
        ).shift(RIGHT * 4.5)
        rt3 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="yellow_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(RIGHT * 1.5, UP * lane_width)
        rt3_text = Text(
            "RT3", color="yellow_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(RIGHT * 1.5, UP * lane_width)
        rt4 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="yellow_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(RIGHT * 0.5, DOWN * lane_width)
        rt4_text = Text(
            "RT4", color="yellow_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(RIGHT * 0.5, DOWN * lane_width)
        rt5 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="yellow_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(RIGHT * 4.0, UP * lane_width)
        rt5_text = Text(
            "RT5", color="yellow_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(RIGHT * 4.0, UP * lane_width)
        rt6 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="yellow_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(RIGHT * 4.5, DOWN * lane_width)
        rt6_text = Text(
            "RT6", color="yellow_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(RIGHT * 4.5, DOWN * lane_width)
        rt7 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="gold_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(LEFT * 3.5)
        rt7_text = Text(
            "RT7", color="gold_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(LEFT * 3.5)
        rt8 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="maroon_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(LEFT * 2.0, UP * lane_width)
        rt8_text = Text(
            "RT8", color="maroon_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(LEFT * 2.0, UP * lane_width)
        rt9 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="maroon_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(LEFT * 2.5, DOWN * lane_width)
        rt9_text = Text(
            "RT9", color="maroon_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(LEFT * 2.5, DOWN * lane_width)
        rt10 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="maroon_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(LEFT * 4.5, UP * lane_width)
        rt10_text = Text(
            "RT10", color="maroon_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(LEFT * 4.5, UP * lane_width)
        rt11 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="maroon_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(LEFT * 5.0, DOWN * lane_width)
        rt11_text = Text(
            "RT11", color="maroon_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(LEFT * 5.0, DOWN * lane_width)
        rt12 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="purple_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(RIGHT * 2.0, UP * (2 * lane_width))
        rt12_text = Text(
            "RT12", color="purple_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(RIGHT * 2.0, UP * (2 * lane_width))
        rt13 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="purple_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(RIGHT * 1.5, DOWN * (2 * lane_width))
        rt13_text = Text(
            "RT13", color="purple_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(RIGHT * 1.5, DOWN * (2 * lane_width))
        rt14 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="purple_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(LEFT * 4.0, UP * (2 * lane_width))
        rt14_text = Text(
            "RT14", color="purple_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(LEFT * 4.0, UP * (2 * lane_width))
        rt15 = Rectangle(
            height=ego_width,
            width=ego_length,
            color="purple_b",
            stroke_width=3.0,
            stroke_opacity=1.0,
        ).shift(LEFT * 2.5, DOWN * (2 * lane_width))
        rt15_text = Text(
            "RT15", color="purple_b", fill_opacity=1.0, stroke_width=0, font_size=18.0
        ).shift(LEFT * 2.5, DOWN * (2 * lane_width))
        self.add(ego, ego_text)
        self.add(edge)
        self.add(rt1, rt2, rt1_text, rt2_text)
        self.add(rt3, rt4, rt3_text, rt4_text)
        self.add(rt5, rt6, rt5_text, rt6_text)
        self.add(rt7, rt7_text)
        self.add(rt8, rt9, rt10, rt11, rt8_text,
                 rt9_text, rt10_text, rt11_text)
        self.add(rt12, rt13, rt14, rt15, rt12_text,
                 rt13_text, rt14_text, rt15_text)
