from manim import *


class ObjRefPoints(Scene):

    def construct(self):

        # title
        text_title = Text(
            "Object Reference Points", font_size=34.0, color=WHITE, stroke_width=0
        ).to_edge(UP, buff=0.5)
        self.add(text_title)

        # coordinate system
        origin = Dot(
            color=WHITE,
            radius=0.05,
            stroke_width=0,
            fill_opacity=1.0,
        ).to_corner(DL, buff=0.5)
        x_axis = Arrow(
            origin.get_center(),
            origin.get_center() + RIGHT * 1.0,
            stroke_width=2,
            buff=0,
            max_tip_length_to_length_ratio=0.11,
            max_stroke_width_to_length_ratio=2,
        )
        X_text = Text(
            "X",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=16.0,
        ).next_to(x_axis, RIGHT, buff=0.1)
        y_axis = Arrow(
            origin.get_center(),
            origin.get_center() + UP * 1.0,
            stroke_width=2,
            buff=0,
            max_tip_length_to_length_ratio=0.11,
            max_stroke_width_to_length_ratio=2,
        )
        Y_text = Text(
            "Y",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=16.0,
        ).next_to(y_axis, UP, buff=0.1)
        sense_of_rotation = Line(
            origin.get_center() + UL * 0.3,
            origin.get_center() + UR * 0.3,
            path_arc=-2.1,
            stroke_width=2,
        ).add_tip(
            tip_length=0.11,
            tip_width=0.11,
        )
        rotation_text = Text(
            "+",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=16.0,
        ).next_to(sense_of_rotation, UR, buff=0.0)
        coordinate_system = Group(
            origin, x_axis, y_axis, sense_of_rotation, X_text, Y_text, rotation_text
        )
        self.add(coordinate_system)

        # add object
        rt_length = 4.0
        rt_width = 2.0
        rt = Rectangle(
            height=rt_length,
            width=rt_width,
            color="blue_c",
            stroke_width=3.5,
            stroke_opacity=1.0,
        )
        rt_head = Line(
            rt.get_center(),
            rt.get_top(),
            color=rt.get_color(),
            stroke_width=rt.get_stroke_width(),
        )
        target = Group(rt, rt_head).shift(LEFT * 2.5)
        self.add(target)

        ref_point_pos = (
            "kRPRearCenter",
            "kRPRearLeft",
            "kRPLeftCenter",
            "kRPFrontLeft",
            "kRPFrontCenter",
            "kRPFrontRight",
            "kRPRightCenter",
            "kRPRearRight",
            "kRPCenter",
        )
        for point in ref_point_pos:
            if point == "kRPRearCenter":
                pos = rt.get_bottom()
                text_dir = DOWN
            if point == "kRPRearLeft":
                pos = rt.get_center() + LEFT * rt_width / 2 + DOWN * rt_length / 2
                text_dir = DL
            if point == "kRPLeftCenter":
                pos = rt.get_left()
                text_dir = LEFT
            if point == "kRPFrontLeft":
                pos = rt.get_center() + LEFT * rt_width / 2 + UP * rt_length / 2
                text_dir = UL
            if point == "kRPFrontCenter":
                pos = rt.get_top()
                text_dir = UP
            if point == "kRPFrontRight":
                pos = rt.get_center() + RIGHT * rt_width / 2 + UP * rt_length / 2
                text_dir = UR
            if point == "kRPRightCenter":
                pos = rt.get_right()
                text_dir = RIGHT
            if point == "kRPRearRight":
                pos = rt.get_center() + RIGHT * rt_width / 2 + DOWN * rt_length / 2
                text_dir = DR
            if point == "kRPCenter":
                pos = rt.get_center()
                text_dir = DOWN
            ref_point = Dot(
                pos,
                color="light_pink",
                fill_opacity=0.5,
                stroke_width=3,
                stroke_color="light_pink",
                radius=0.11,
            )
            ref_num = Text(
                str(ref_point_pos.index(point)),
                color="light_pink",
                fill_opacity=1.0,
                stroke_width=0,
                font_size=24.0,
            ).next_to(
                ref_point,
                direction=text_dir,
                buff=0.2,
            )
            self.add(ref_point, ref_num)

            code = """
enum RefPoint : uint8_t {
  kRPRearCenter = 0U,
  kRPRearLeft = 1U,
  kRPLeftCenter = 2U,
  kRPFrontLeft = 3U,
  kRPFrontCenter = 4U, 
  kRPFrontRight = 5U, 
  kRPRightCenter = 6U,
  kRPRearRight = 7U,
  kRPCenter = 8U,
  kRPUndetermined = 9U
};
"""
            ref_point_code = Code(
                code=code,
                language="cpp",
                line_spacing=0.6,
                font_size=16,
                font="Monospace",
                tab_width=4,
                background="window",
                background_stroke_width=2,
                background_stroke_color="white",
                insert_line_no=True,
                # style=Code.styles_list[15],
            ).to_edge(RIGHT, buff=1)
            self.add(ref_point_code)
