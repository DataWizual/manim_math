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
        s_q = VGroup(s_text_1, q_text_1)
        # Part 3 First, let's designate all the points
        e_right_dot = self.dots(-1.4, 0, None, YELLOW, True)
        base_line = self.lines(a_left_dot,
                               e_right_dot, '#eb0a1e', Line, True)
        base_line_center = base_line.get_center()
        o_center_dot = self.dots(None, None, base_line_center, YELLOW, False)
        b_triangle_dot = self.dots(-4.28, 0, None, '#00ff00', True)
        d_triangle_dot = self.dots(-4.95, 1.34, None, '#00ff00', True)
        c_triangle_dot = self.dots(-1.9, 1.34, None, '#00ff00', True)

        line_dot = VGroup(a_left_dot, e_right_dot,  o_center_dot,
                          b_triangle_dot, d_triangle_dot, c_triangle_dot)

        o = self.texts(Tex, r"O", '#00ff00', o_center_dot,
                       None, None, DOWN, False, 0.2)
        a = self.texts(Tex, r"A", '#00ff00', a_left_dot,
                       None, None, DOWN, False, 0.2)
        b = self.texts(Tex, r"B", '#00ff00', b_triangle_dot,
                       None, None, DOWN, False, 0.2)
        c = self.texts(Tex, r"C", '#00ff00', c_triangle_dot,
                       None, None, UP, False, 0.2)
        d = self.texts(Tex, r"D", '#00ff00', d_triangle_dot,
                       None, None, UP, False, 0.2)
        e = self.texts(Tex, r"E", '#00ff00', e_right_dot,
                       None, None, DOWN, False, 0.2)

        verts = VGroup(o, a, b, c, d, e)

        # Part 7 Draw perpendicular lines from point D and C to the diameter
        p_dot = self.dots(-4.95, 0, None, '#00ff00', True)
        f_dot = self.dots(-1.9, 0, None, '#00ff00', True)

        p = self.texts(Tex, r"P", '#00ff00', p_dot,
                       None, None, DOWN, False, 0.2)
        f = self.texts(Tex, r"F", '#00ff00', f_dot,
                       None, None, DOWN, False, 0.2)

        auxiliary_dots = VGroup(
            p_dot, p, f_dot, f)

        dashed_line_d_p = self.lines(d_triangle_dot,
                                     p_dot, YELLOW, DashedLine, False)
        dashed_line_c_f = self.lines(c_triangle_dot,
                                     f_dot, YELLOW, DashedLine, False)

        c_f_line = self.lines(c_triangle_dot, f_dot, YELLOW, Line, True)

        d_p_line = self.lines(
            d_triangle_dot, p_dot, YELLOW, Line, True)

        similar = self.texts(
            MathTex, r"\triangle BDP\sim \triangle DCF", None, None, 1, 2, None, True, None)
        similar[0][0].set_color(YELLOW)
        similar[0][1:4].set_color('#00ff00')
        similar[0][5].set_color(YELLOW)
        similar[0][6:9].set_color('#00ff00')

        similar_f = self.texts(
            MathTex, r"\frac{BP}{DP}= \frac{CF}{BF}", None, similar, None, None, DOWN, False, 0.5)
        similar_f[0][0:2].set_color('#00ff00')
        similar_f[0][3:5].set_color('#00ff00')
        similar_f[0][6:8].set_color('#00ff00')
        similar_f[0][9:11].set_color('#00ff00')
        similar_f.align_to(similar, LEFT)

        # Part 8 Let us denote the distances from the center to the
        #        points of tangency of the perpendiculars by the letter x
        d_c_line = self.lines(
            d_triangle_dot, c_triangle_dot, YELLOW, Line, True)
        x_text = self.texts(
            Tex, r"2x", '#f6d800', d_c_line, None, None, UP, False, 0.2)

        # Part 9 Let us denote the dimensions of the perpendiculars by
        # the letter y
        y_text_1 = self.texts(
            Tex, r"y", '#f6d800', d_p_line, None, None, LEFT, False, 0.2)
        y_text_2 = self.texts(
            Tex, r"y", '#f6d800', c_f_line, None, None, RIGHT, False, 0.2)

        y_text = VGroup(y_text_1, y_text_2)

        # Part 10 Distance BP = OP – OB = x – 2; Distance BF = OF + OB = x + 2
        # left
        b_p = self.texts(
            MathTex, r"BP = x – 2", None, similar_f, None, None, DOWN, False, 0.5)
        b_p[0][0:2].set_color('#00ff00')
        b_p[0][3].set_color(BLUE)
        b_p[0][5].set_color(BLUE)
        b_p.align_to(similar, LEFT)

        # right
        b_f = self.texts(
            MathTex, r"BF = x + 2", None, b_p, None, None, DOWN, False, 0.5)
        b_f[0][0:2].set_color('#00ff00')
        b_f[0][3].set_color(BLUE)
        b_f[0][5].set_color(BLUE)
        b_f.align_to(similar, LEFT)

        # formula \frac{x-2}{y}= \frac{y}{x+2}
        rightarrow = self.texts(
            MathTex, r"\Rightarrow", None, similar_f, None, None, RIGHT, False, 0.5)
        formula_simulate = self.texts(
            MathTex, r"\frac{x-2}{y}= \frac{y}{x+2}", None, rightarrow, None, None, RIGHT, False, 0.5)
        formula_simulate[0][0].set_color(YELLOW)
        formula_simulate[0][2].set_color(BLUE)
        formula_simulate[0][4].set_color(YELLOW)
        formula_simulate[0][6].set_color(YELLOW)
        formula_simulate[0][8].set_color(YELLOW)
        formula_simulate[0][10].set_color(BLUE)

        # formula y^{2}=\left ( x-2 \right )\left ( x+2 \right )
        formula_y = self.texts(
            MathTex, r"y^{2}=\left ( x-2 \right )\left ( x+2 \right )", None, formula_simulate, None, None, DOWN, False, 0.5)
        formula_y[0][0].set_color(YELLOW)
        formula_y[0][4].set_color(YELLOW)
        formula_y[0][6].set_color(BLUE)
        formula_y[0][9].set_color(YELLOW)
        formula_y[0][11].set_color(BLUE)
        formula_y.align_to(formula_simulate, LEFT)

        # Part 11 \left ( a-b \right )\left ( a+b \right )= a^{2}-b^{2}
        identity = self.texts(MathTex, r"\left ( a-b \right )\left ( a+b \right )= a^{2}-b^{2}",
                              None, None, 4.5, 3, None, True, None)
        identity.set_color(ORANGE)
        under = Underline(identity)
        identity_under = VGroup(identity, under)

        # Part 12
        y_square = self.texts(MathTex, r"y^{2}= x^{2}-4",
                              None, formula_y, None, None, DOWN, False, 0.5)
        y_square[0][0].set_color(YELLOW)
        y_square[0][3].set_color(YELLOW)
        y_square[0][6].set_color(BLUE)
        y_square.align_to(formula_simulate, LEFT)

        y_square_surround = SurroundingRectangle(y_square, color='#ff00ff')
        y_1 = VGroup(y_square, y_square_surround)

        y_square_s = self.texts(MathTex, r"y^{2}= x^{2}-4",
                                None, None, 4.5, 3, None, True, 0.5)
        y_square_s[0][0].set_color(YELLOW)
        y_square_s[0][3].set_color(YELLOW)
        y_square_s[0][6].set_color(BLUE)
        y_square_s_surround = SurroundingRectangle(y_square_s, color='#ff00ff')
        y_2 = VGroup(y_square_s, y_square_s_surround)

        # Part 13 Draw another radius from the center of the semicircle to point D
        # (, left, right, color, type_line, choise)
        o_d_radius = self.lines(
            o_center_dot, d_triangle_dot, '#eb0a1e', Line, True)
        r_text = self.texts(Tex, r"r=8", None,
                            None, -3.8, 0.8, None, True, 0.2)
        r_text[0][0].set_color(YELLOW)
        r_text[0][2].set_color('#0000ff')

        x_text_1 = self.texts(Tex, r"x", YELLOW,
                              b_triangle_dot, None, None, UP, False, 0.2)

        x_y_r_copy = VGroup(
            x_text_1.copy(), y_text_1.copy(), r_text[0][0].copy())

        o_d_triangle = self.lines(
            o_center_dot, d_triangle_dot, '#eb0a1e', Line, True)
        d_p_triangle = self.lines(
            d_triangle_dot, p_dot, '#eb0a1e', Line, True)
        p_b_triangle = self.lines(
            p_dot, o_center_dot, '#eb0a1e', Line, True)

        o_p_b_gr = VGroup(o_d_triangle, d_p_triangle, p_b_triangle)

        # Part 14 Apply the Pythagorean theorem to the resulting rectangle
        pythagorean_t = self.texts(MathTex, r"a^{2}+b^{2}= c^{2}",
                                   None, None, 1, 2, None, True, None)
        pythagorean_t.set_color(ORANGE)
        pythagorean_under_line = Underline(pythagorean_t)
        pythagorean_under = VGroup(pythagorean_t, pythagorean_under_line)

        # Part 15 Put the values of the sides of a right triangle into the formula
        x_y_r = self.texts(MathTex, r"x^{2}+y^{2}= r^{2}",
                           None, pythagorean_under, None, None, DOWN, False, 0.5)
        x_y_r[0][0].set_color(YELLOW)
        x_y_r[0][3].set_color(YELLOW)
        x_y_r[0][6].set_color(YELLOW)
        x_y_r.align_to(pythagorean_under, LEFT)

        #  x^2+x^2-4=64
        x_y_r_1 = self.texts(MathTex, r"x^{2}+x^{2}-4=64",
                             None, x_y_r, None, None, DOWN, False, 0.5)
        x_y_r_1[0][0].set_color(YELLOW)
        x_y_r_1[0][3].set_color(YELLOW)
        x_y_r_1[0][6].set_color(BLUE)
        x_y_r_1[0][8:10].set_color(BLUE)
        x_y_r_1.align_to(pythagorean_under, LEFT)

        # 2x^2-4=64
        x_y_r_2 = self.texts(MathTex, r"2x^{2}-4=64",
                             None, x_y_r_1, None, None, DOWN, False, 0.5)
        x_y_r_2[0][0].set_color(BLUE)
        x_y_r_2[0][1].set_color(YELLOW)
        x_y_r_2[0][4].set_color(BLUE)
        x_y_r_2[0][6:8].set_color(BLUE)
        x_y_r_2.align_to(pythagorean_under, LEFT)

        # +4
        minus_4 = self.texts(MathTex, r"+ 4", None,
                             x_y_r_2[0][3], None, None, DOWN, False, 0.2)
        minus_4.set_color(ORANGE)
        minus_4.align_to(x_y_r_2[0][3], LEFT)
        minus_4_copy = self.texts(MathTex, r"+ 4", None,
                                  minus_4, None, None, RIGHT, False, 0.5)
        minus_4_copy.set_color(ORANGE)
        minus_gr = VGroup(minus_4, minus_4_copy)

        # 2x^2=68
        x_y_r_3 = self.texts(MathTex, r"2x^{2}=68",
                             None, x_y_r_2, None, None, DOWN, False, 0.5)
        x_y_r_3[0][0].set_color(BLUE)
        x_y_r_3[0][1].set_color(YELLOW)
        x_y_r_3[0][4:6].set_color(BLUE)
        x_y_r_3.align_to(pythagorean_under, LEFT)

        # :2
        x_y_r_4 = self.texts(MathTex, r"\frac{2x^{2}}{2}=\frac{68}{2}",
                             None, pythagorean_under, None, None, 3*RIGHT, False, 0.5)
        x_y_r_4[0][0].set_color(BLUE)
        x_y_r_4[0][1].set_color(YELLOW)
        x_y_r_4[0][4].set_color(ORANGE)
        x_y_r_4[0][6:8].set_color(BLUE)
        x_y_r_4[0][9].set_color(ORANGE)

        # Part 16 x^2=34
        x_y_r_5 = self.texts(MathTex, r"x^{2}=34",
                             None, x_y_r_4, None, None, DOWN, False, 0.5)
        x_y_r_5[0][0].set_color(YELLOW)
        x_y_r_5[0][3:5].set_color(BLUE)
        x_y_r_5.align_to(x_y_r_4, LEFT)

        # Part 17 x=√34
        x_y_r_6 = self.texts(MathTex, r"\sqrt{x^{2}}= \sqrt{34}",
                             None, x_y_r_5, None, None, DOWN, False, 0.5)
        x_y_r_6[0][2].set_color(YELLOW)
        x_y_r_6[0][7:9].set_color(BLUE)
        x_y_r_6.align_to(x_y_r_4, LEFT)

        x_y_r_7 = self.texts(MathTex, r"x= \sqrt{34}",
                             None, x_y_r_6, None, None, DOWN, False, 0.5)
        x_y_r_7[0][0].set_color(YELLOW)
        x_y_r_7[0][4:6].set_color(BLUE)
        x_y_r_7.align_to(x_y_r_4, LEFT)
        x_surround = SurroundingRectangle(x_y_r_7, color='#ff00ff')

        # part 1
        self.add(task_text_1)
        self.add(img)

        # part 2
        self.add(s_q)
        self.add(q_text_1)

        # part 3
        self.add(line_dot)
        self.add(verts)

        # # part 7
        self.add(auxiliary_dots)
        self.add(dashed_line_d_p)
        self.add(dashed_line_c_f)
        # ******************************
        self.add(similar)
        self.add(similar_f)

        # Part 8
        self.add(x_text)

        # Part 9
        self.add(y_text)

        # Part 10
        # left
        self.add(b_p)

        # right
        self.add(b_f)

        # formula \frac{x-2}{y}= \frac{y}{x+2}
        self.add(rightarrow)
        self.add(formula_simulate)

        # formula y^{2}=\left ( x-2 \right )\left ( x+2 \right )
        self.add(formula_y)
        self.add(y_1)
        self.add(identity_under)

        self.wait(2)

        self.play(FadeOut(similar, similar_f, b_p,
                  b_f, rightarrow, formula_simulate, formula_y, identity_under), run_time=1)
        self.play(Transform(y_1, y_2), run_time=2)

        # Part 13
        self.play(FadeOut(s_q))
        # self.add(o_d_radius)
        self.play(Create(o_d_radius), run_time=2)
        # self.add(r_text)
        self.play(Write(r_text), run_time=2)
        # self.add(x_text_1)
        self.play(Write(x_text_1), run_time=2)
        self.play(FadeIn(pythagorean_under), run_time=2)  # Part 14
        # self.add(pythagorean_under)
        self.play(FadeIn(o_p_b_gr), run_time=2)
        self.play(Indicate(o_p_b_gr), run_time=3)
        self.play(FadeOut(o_p_b_gr), run_time=2)
        # self.add(x_y_r)
        self.play(Transform(x_y_r_copy, x_y_r), run_time=3)
        self.play(Transform(x_y_r[0][0:2].copy(), x_y_r_1[0][0:2]), run_time=3)
        # self.add(x_y_r_1[0][2])
        self.play(Create(x_y_r_1[0][2]), run_time=1)
        y_2_gr = VGroup(x_y_r[0][3:5], y_square_s)
        self.play(Indicate(y_2_gr), run_time=3)
        # self.add(x_y_r_1)
        self.play(
            Transform(y_square_s[0][3:7].copy(), x_y_r_1[0][3:7]), run_time=3)
        # self.add(x_y_r_1[0][7])
        self.play(Create(x_y_r_1[0][7]), run_time=1)
        self.play(
            Transform(r_text[0][2].copy(), x_y_r_1[0][8:10]), run_time=3)
        # self.add(x_y_r_2)
        self.play(
            Transform(x_y_r_1.copy(), x_y_r_2), run_time=3)
        # self.add(minus_gr)
        self.play(Write(minus_gr), run_time=1)
        # self.add(x_y_r_3)
        self.play(
            Transform(x_y_r_2.copy(), x_y_r_3), run_time=3)
        # self.add(x_y_r_4)
        self.wait(1)
        self.play(
            Transform(x_y_r_3.copy(), x_y_r_4), run_time=3)
        # self.add(x_y_r_5)
        self.wait(1)
        self.play(
            Transform(x_y_r_4.copy(), x_y_r_5), run_time=3)
        # self.add(x_y_r_6)
        self.wait(1)
        self.play(
            Transform(x_y_r_5.copy(), x_y_r_6), run_time=3)
        # self.add(x_y_r_7)
        self.wait(1)
        self.play(
            Transform(x_y_r_6.copy(), x_y_r_7), run_time=3)
        # self.add(x_surround)
        self.wait(1)
        self.play(Create(x_surround), run_time=1)

        self.wait(2)

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
