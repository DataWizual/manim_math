from manim import *


class Triangle(Scene):
    def construct(self):
        # Part 1 We have semicircle, and inside is a right triangle
        task_text_1 = Tex(
            r"Find Area of the BLUE right triangle:", font_size=32)
        task_text_1.set_color(YELLOW)
        task_text_1[0][13:17].set_color(BLUE)
        task_text_1.set_x(-3).set_y(3)

        a_left_dot = self.dots(-5.5, 0, None, YELLOW, True)
        img = ImageMobject("triangle.png")
        img.next_to(a_left_dot.get_center(), RIGHT+UP, buff=-0.025)

        # Part 2 We need to find the area of this right triangle
        s_text_1 = self.texts(
            MathTex, r"S_{t}", YELLOW, None, -4, 0.8, None, True, None)
        s_text_1.set_color(YELLOW)

        q_text_1 = self.texts(Tex, r"-?", '#eb0a1e',
                              s_text_1, None, None, RIGHT, False, 0.2)

        # Part 3 First, let's designate all the points
        e_right_dot = self.dots(-1.4, 0, None, YELLOW, True)
        base_line = self.lines(a_left_dot,
                               e_right_dot, '#eb0a1e', Line, True)
        base_line_center = base_line.get_center()
        o_center_dot = self.dots(None, None, base_line_center, YELLOW, False)
        b_triangle_dot_1 = self.dots(-4.28, 0, None, '#00ff00', True)
        d_triangle_dot_2 = self.dots(-4.95, 1.34, None, '#00ff00', True)
        c_triangle_dot_3 = self.dots(-1.9, 1.34, None, '#00ff00', True)

        line_dot = VGroup(a_left_dot, e_right_dot,  o_center_dot,
                          b_triangle_dot_1, d_triangle_dot_2, c_triangle_dot_3)

        o = self.texts(Tex, r"O", '#00ff00', o_center_dot,
                       None, None, DOWN, False, 0.2)
        a = self.texts(Tex, r"A", '#00ff00', a_left_dot,
                       None, None, DOWN, False, 0.2)
        b = self.texts(Tex, r"B", '#00ff00', b_triangle_dot_1,
                       None, None, DOWN, False, 0.2)
        c = self.texts(Tex, r"C", '#00ff00', c_triangle_dot_3,
                       None, None, UP, False, 0.2)
        d = self.texts(Tex, r"D", '#00ff00', d_triangle_dot_2,
                       None, None, UP, False, 0.2)
        e = self.texts(Tex, r"E", '#00ff00', e_right_dot,
                       None, None, DOWN, False, 0.2)

        verts = VGroup(o, a, b, c, d, e)

        # Part 4 The distances from the point of tangency of a right triangle with
        #        a diameter to the left and right sides of the semicircle are given
        brace_1 = self.braces(Line(a, b), r"6", True, None)
        brace_2 = self.braces(Line(b, e), r"10", True, None)
        braces = VGroup(brace_1, brace_2)

        a_b_dist = self.texts(MathTex, r"AB = 6",
                              None, None, 0, 2, None, True, None)
        a_b_dist[0][0:2].set_color('#00ff00')
        a_b_dist[0][3].set_color('#ff00ff')

        b_e_dist = self.texts(MathTex, r"BE = 10", None,
                              a_b_dist, None, None, DOWN, False, 0.5)
        b_e_dist[0][0:2].set_color('#00ff00')
        b_e_dist[0][3:5].set_color('#ff00ff')

        given = VGroup(a_b_dist, b_e_dist)

        # Part 5 From these distances we get
        brace_diametr = self.braces(Line(a, e), r"D", True, None)
        diametr_text = self.texts(
            Tex, r"The diameter is:", '#f6d800', b_e_dist, None, None, DOWN, False, 0.5)
        diametr_text.align_to(a_b_dist, LEFT)

        diametr = self.texts(MathTex, r"D = AE = 16", None,
                             diametr_text, None, None, RIGHT, False, 0.2)
        diametr[0][0].set_color(YELLOW)
        diametr[0][2:4].set_color('#00ff00')
        diametr[0][5:7].set_color(BLUE)

        diametr_gr = VGroup(diametr_text, diametr)

        brace_radius_1 = self.braces(Line(a, o), r"r", True, None)
        brace_radius_2 = self.braces(Line(o, e), r"r", True, None)
        brace_radius = VGroup(brace_radius_1, brace_radius_2)
        radius_text = self.texts(
            Tex, r"The radius is:", '#f6d800', diametr_text, None, None, DOWN, False, 0.5)
        radius_text.align_to(a_b_dist, LEFT)

        radius = self.texts(MathTex, r"r = OA = OE = 8", None,
                            radius_text, None, None, RIGHT, False, 0.2)
        radius[0][0].set_color(YELLOW)
        radius[0][2:4].set_color('#00ff00')
        radius[0][5:7].set_color('#00ff00')
        radius[0][8].set_color(BLUE)
        radius.align_to(diametr, LEFT)

        radius_gr = VGroup(radius_text, radius)

        # Part 6 Distance from center to point of contact OB = r – 6 = 2
        brace_o_b = self.braces(Line(b, o), r"OB", True, None)
        o_b_dist = self.texts(
            MathTex, r"\\OB=r–6=2", None, radius_text, None, None, DOWN, False, 0.5)
        o_b_dist[0][0:2].set_color('#00ff00')
        o_b_dist[0][3].set_color(YELLOW)
        o_b_dist[0][5].set_color(BLUE)
        o_b_dist[0][7].set_color(BLUE)
        o_b_dist.align_to(radius_text, LEFT)

        # part 1
        self.play(Write(task_text_1))
        self.add(img)

        # part 2
        self.play(Write(s_text_1))
        self.play(Write(q_text_1))

        # part 3
        self.play(Create(line_dot))
        self.play(Write(verts))

        # part 4
        self.play(Create(braces), run_time=2)
        self.play(
            Transform(brace_1, a_b_dist), run_time=2)
        self.play(
            Transform(brace_2, b_e_dist), run_time=2)

        # part 5
        self.play(Write(brace_diametr), run_time=2)
        self.play(
            Transform(brace_diametr, diametr_gr), run_time=2)
        self.play(Write(brace_radius), run_time=2)
        self.play(
            Transform(brace_radius, radius_gr), run_time=2)

        # part 6
        self.play(Write(brace_o_b), run_time=2)
        self.play(
            Transform(brace_o_b, o_b_dist), run_time=2)

    def dots(self, x, y, moveto, color, choise):
        if choise:
            dot_a = Dot(color=color)
            dot_a.scale(0.5)
            dot_a.set_x(x).set_y(y)
        else:
            dot_a = Dot(color=color)
            dot_a.scale(0.5)
            dot_a.move_to(moveto)
        return dot_a

    def lines(self, left, right, color, type_line, choise):
        if choise:
            line_s = type_line(left.get_center(),
                               right.get_center(), color=color)
        else:
            line_s = type_line(left.get_center(),
                               right.get_center(), color=color)
        return line_s

    def texts(self, func, text, color, nextto, x, y, side, choice, buff):
        if choice:
            text_v = func(text, font_size=32)
            text_v.set_x(x).set_y(y)
        else:
            text_v = func(text, color=color, font_size=32)
            text_v.next_to(nextto, side, buff=buff)
        return text_v

    def braces(self, dist, text, choice, rotate):
        if choice:
            brace_h = BraceText(dist, text=text)
            return brace_h
        else:
            brace_v = Brace(dist, direction=dist.copy().rotate(
                rotate).get_unit_vector())
            brace_v_text = brace_v.get_text(text)
            return brace_v, brace_v_text
