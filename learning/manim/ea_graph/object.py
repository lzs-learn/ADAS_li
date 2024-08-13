from manim import *


class Object(Scene):

    def construct(self):
        # * add lines
        lane_stroke_width = 2
        lane_width = 0.9
        half_lane_width = 0.45
        host_lane_center = LEFT * (4 * lane_width)
        line_num = 6
        for i in range(line_num):
            if i == 0 or i == 5:
                line = Line(DOWN * 4.0, UP * 4.0, stroke_width=lane_stroke_width)
            else:
                line = DashedLine(
                    DOWN * 4.0,
                    UP * 4.0,
                    dash_length=0.6,
                    dashed_ratio=0.6,
                    stroke_width=lane_stroke_width - 0.5,
                )
            line.shift(LEFT * (6.5 - i) * lane_width)
            self.add(line)

        # * add ego
        ego_length = 1.1
        ego_width = 0.5
        ego_stroke_width = 3.0
        ego_stroke_opacity = 1.0

        ego = Rectangle(
            height=ego_length,
            width=ego_width,
            color="blue_d",
            stroke_width=ego_stroke_width,
            stroke_opacity=ego_stroke_opacity,
        ).shift(host_lane_center + DOWN * 2)
        ego_rear_axle = Line(
            ego.get_left(),
            ego.get_right(),
            color="blue_d",
            stroke_width=ego_stroke_width - 1.5,
            stroke_opacity=1.0,
        ).shift(DOWN * 0.25 * ego_length)
        ego_ref_center = Dot(
            color="blue_d",
            radius=0.04,
            stroke_width=0,
            fill_opacity=1.0,
        ).move_to(ego_rear_axle.get_center())
        ego_text = Text(
            "ego", fill_opacity=0.7, stroke_width=0, font_size=14.0
        ).move_to(ego.get_center())
        self.add(ego, ego_rear_axle, ego_ref_center, ego_text)

        # * add coordinate system
        origin = Dot(
            color=WHITE,
            radius=0.05,
            stroke_width=0,
            fill_opacity=1.0,
        ).to_corner(DL, buff=0.2)
        y_axis = Arrow(
            origin.get_center(),
            origin.get_center() + RIGHT * 0.8,
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
        ).next_to(y_axis, RIGHT, buff=0.1)
        x_axis = Arrow(
            origin.get_center(),
            origin.get_center() + UP * 0.8,
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
        ).next_to(x_axis, UP, buff=0.1)
        sense_of_rotation = Line(
            origin.get_center() + UL * 0.2,
            origin.get_center() + UR * 0.2,
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
        ).scale(0.8)
        self.add(coordinate_system)

        # * add vision object
        vision_obj_length = 1.1
        vision_obj_width = 0.5
        vision_obj_stroke_width = 3.0
        vision_obj_stroke_opacity = 1.0

        vision_obj = Rectangle(
            height=vision_obj_length,
            width=vision_obj_width,
            color="gold_c",
            stroke_width=vision_obj_stroke_width,
            stroke_opacity=vision_obj_stroke_opacity,
        ).shift((host_lane_center + lane_width) + UP * 2)
        vision_obj_head = Line(
            vision_obj.get_top(),
            vision_obj.get_bottom() + UP * 0.3 * vision_obj_length,
            color="gold_c",
            stroke_width=vision_obj_stroke_width - 1,
            stroke_opacity=1.0,
        )
        vision_obj_ref_center = Dot(
            color="gold_c",
            radius=0.05,
            stroke_width=0,
            fill_opacity=1.0,
        ).move_to(vision_obj.get_center())
        self.add(vision_obj, vision_obj_head, vision_obj_ref_center)

        # * Add radar object
        radar_obj_length = 0.15
        radar_obj_width = 0.15
        radar_obj_stroke_width = 3.0
        radar_obj_stroke_opacity = 1.0

        radar_obj = Rectangle(
            height=radar_obj_length,
            width=radar_obj_width,
            color="light_pink",
            stroke_width=radar_obj_stroke_width,
            stroke_opacity=radar_obj_stroke_opacity,
        ).shift((host_lane_center + lane_width - 0.1) + UP * 1.4)
        radar_obj_ref_center = Dot(
            color="light_pink",
            radius=0.02,
            stroke_width=0,
            fill_opacity=1.0,
        ).move_to(radar_obj.get_center())
        self.add(radar_obj, radar_obj_ref_center)

        # play coordinate
        ego_y_axis = Arrow(
            ego_ref_center.get_center(),
            ego_ref_center.get_center() + RIGHT * 2.0,
            stroke_width=2,
            buff=0,
            tip_shape=StealthTip,
            max_tip_length_to_length_ratio=0.05,
            max_stroke_width_to_length_ratio=1,
        )
        ego_x_axis = Line(
            ego_ref_center.get_center(),
            ego_ref_center.get_center() + UP * 2.0,
            stroke_width=2,
            buff=0,
        ).add_tip(
            tip_length=0.1,
            tip_width=1,
            tip_shape=StealthTip,
        )
        ego_sense_of_rotation = Line(
            ego_ref_center.get_center() + UP * 1.2 + LEFT * 0.3,
            ego_ref_center.get_center() + UP * 1.2 + RIGHT * 0.3,
            path_arc=-2.1,
            stroke_width=2,
        ).add_tip(
            tip_length=0.1,
            tip_width=1,
            tip_shape=StealthTip,
        )
        self.play(GrowFromPoint(ego_x_axis, ego_x_axis.get_start()))
        self.play(GrowArrow(ego_y_axis))
        self.play(Create(ego_sense_of_rotation))
        self.wait(1.0)

        # * Add Class
        adjust_scale = 0.5
        aligned_buff = 0.2

        ID_text = Text(
            "ID",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=30.0,
        ).move_to(UP * 2.0 + RIGHT * 1.0)
        self.play(GrowFromPoint(ID_text, vision_obj.get_center()))
        self.wait(1.0)
        self.play(
            ID_text.animate.to_edge(UP, buff=0.25)
            .scale(adjust_scale)
            .to_edge(RIGHT, buff=1.2)
        )

        valid_status_text = Text(
            "valid_status",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=30.0,
        ).move_to(UP * 2.0 + RIGHT * 1.0)
        self.play(GrowFromPoint(valid_status_text, vision_obj.get_center()))
        self.wait(1.0)
        self.play(
            valid_status_text.animate.to_edge(UP, buff=0.25)
            .scale(adjust_scale)
            .next_to(ID_text, direction=DOWN, buff=aligned_buff, aligned_edge=LEFT)
        )

        source_text = Text(
            "source",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=30.0,
        ).move_to(UP * 2.0 + RIGHT * 1.0)
        self.play(GrowFromPoint(source_text, vision_obj.get_center()))
        self.wait(1.0)
        self.play(
            source_text.animate.to_edge(UP, buff=0.25)
            .scale(adjust_scale)
            .next_to(
                valid_status_text, direction=DOWN, buff=aligned_buff, aligned_edge=LEFT
            )
        )

        motion_status_text = Text(
            "motion_status",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=30.0,
        ).move_to(UP * 2.0 + RIGHT * 1.0)
        self.play(GrowFromPoint(motion_status_text, vision_obj.get_center()))
        self.wait(1.0)
        self.play(
            motion_status_text.animate.to_edge(UP, buff=0.25)
            .scale(adjust_scale)
            .next_to(source_text, direction=DOWN, buff=aligned_buff, aligned_edge=LEFT)
        )

        motion_text = Text(
            "motion",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=30.0,
        ).move_to(UP * 2.0 + RIGHT * 1.0)
        self.play(GrowFromPoint(motion_text, vision_obj.get_center()))
        self.wait(1.0)
        self.play(
            motion_text.animate.to_edge(UP, buff=0.25)
            .scale(adjust_scale)
            .next_to(
                motion_status_text, direction=DOWN, buff=aligned_buff, aligned_edge=LEFT
            )
        )

        classification_text = Text(
            "classification",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=30.0,
        ).move_to(UP * 2.0 + RIGHT * 1.0)
        self.play(GrowFromPoint(classification_text, vision_obj.get_center()))
        self.wait(1.0)
        self.play(
            classification_text.animate.to_edge(UP, buff=0.25)
            .scale(adjust_scale)
            .next_to(motion_text, direction=DOWN, buff=aligned_buff, aligned_edge=LEFT)
        )

        class_prob_text = Text(
            "class_prob",
            fill_opacity=1.0,
            stroke_width=0,
            font_size=30.0,
        ).move_to(UP * 2.0 + RIGHT * 1.0)
        self.play(GrowFromPoint(class_prob_text, vision_obj.get_center()))
        self.wait(1.0)
        self.play(
            class_prob_text.animate.to_edge(UP, buff=0.25)
            .scale(adjust_scale)
            .next_to(
                classification_text,
                direction=DOWN,
                buff=aligned_buff,
                aligned_edge=LEFT,
            )
        )
