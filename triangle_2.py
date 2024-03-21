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

        # Part 4 The distances from the point of tangency of a right triangle with
        #        a diameter to the left and right sides of the semicircle are given
        brace_1 = self.braces(Line(a, b), r"6", True, None)
        brace_2 = self.braces(Line(b, e), r"10", True, None)

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
        diametr_text = self.texts(
            Tex, r"The diameter is:", '#f6d800', b_e_dist, None, None, DOWN, False, 0.5)
        diametr_text.align_to(a_b_dist, LEFT)

        diametr = self.texts(MathTex, r"D = AE = 16", None,
                             diametr_text, None, None, RIGHT, False, 0.2)
        diametr[0][0].set_color(YELLOW)
        diametr[0][2:4].set_color('#00ff00')
        diametr[0][5:7].set_color(BLUE)

        diametr_gr = VGroup(diametr_text, diametr)

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
        o_b_dist = self.texts(
            MathTex, r"\\OB=r–6=2", None, radius_text, None, None, DOWN, False, 0.5)
        o_b_dist[0][0:2].set_color('#00ff00')
        o_b_dist[0][3].set_color(YELLOW)
        o_b_dist[0][5].set_color(BLUE)
        o_b_dist[0][7].set_color(BLUE)
        o_b_dist.align_to(radius_text, LEFT)

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
        c_b_line = self.lines(
            c_triangle_dot, b_triangle_dot, YELLOW, Line, True)
        b_f_line = self.lines(
            b_triangle_dot, f_dot, YELLOW, Line, True)

        right_rightangle = Square(side_length=0.2, color=YELLOW)
        right_rightangle.next_to(f_dot.get_center(), UL, buff=0)

        right_triangle = VGroup(c_f_line, c_b_line, b_f_line, right_rightangle)

        d_b_line = self.lines(
            d_triangle_dot, b_triangle_dot, YELLOW, Line, True)
        d_p_line = self.lines(
            d_triangle_dot, p_dot, YELLOW, Line, True)
        b_p_line = self.lines(
            b_triangle_dot, p_dot, YELLOW, Line, True)

        left_rightangle = Square(side_length=0.2, color=YELLOW)
        left_rightangle.next_to(p_dot.get_center(), UR, buff=0)

        left_triangle = VGroup(d_b_line, d_p_line, b_p_line, left_rightangle)

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

        brace_x_1 = self.braces(Line(p_dot, o_center_dot), r"x", True, None)
        brace_x_2 = self.braces(Line(o_center_dot, f_dot), r"x", True, None)
        brace_x = VGroup(brace_x_1, brace_x_2)
        d_c_line = self.lines(
            d_triangle_dot, c_triangle_dot, YELLOW, Line, True)
        x_text = self.texts(
            Tex, r"2x", '#f6d800', d_c_line, None, None, UP, False, 0.2)

        # Part 9 Let us denote the dimensions of the perpendiculars by
        # the letter y
        brace_y_1, brace_y_1_text = self.braces(
            Line(p_dot, d_triangle_dot), r"y", False, PI / 2)
        brace_y_2, brace_y_2_text = self.braces(
            Line(f_dot, c_triangle_dot), r"y", False, -(PI / 2))

        brace_y = VGroup(brace_y_1, brace_y_1_text, brace_y_2, brace_y_2_text)

        y_text_1 = self.texts(
            Tex, r"y", '#f6d800', d_p_line, None, None, LEFT, False, 0.2)
        y_text_2 = self.texts(
            Tex, r"y", '#f6d800', c_f_line, None, None, RIGHT, False, 0.2)

        y_text = VGroup(y_text_1, y_text_2)

        # Part 10 Distance BP = OP – OB = x – 2; Distance BF = OF + OB = x + 2
        # left
        b_p_brace = self.braces(
            Line(p_dot, b_triangle_dot), r"x-2", True, None)
        b_p = self.texts(
            MathTex, r"BP = x – 2", None, similar_f, None, None, DOWN, False, 0.5)
        b_p[0][0:2].set_color('#00ff00')
        b_p[0][3].set_color(BLUE)
        b_p[0][5].set_color(BLUE)
        b_p.align_to(similar, LEFT)

        # right
        b_f_brace = self.braces(
            Line(b_triangle_dot, f_dot), r"x+2", True, None)
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
        y_square[0][0:2].set_color(YELLOW)
        y_square[0][3:6].set_color(YELLOW)
        y_square[0][6].set_color(BLUE)
        y_square.align_to(formula_simulate, LEFT)

        y_square_surround = SurroundingRectangle(y_square, color='#ff00ff')

        # part 1
        self.add(task_text_1)
        self.add(img)

        # part 2
        self.add(s_text_1)
        self.add(q_text_1)

        # part 3
        self.add(line_dot)
        self.add(verts)

        # part 4
        self.add(given)

        # # part 5
        self.add(diametr_gr)
        self.add(radius_gr)

        # # part 6
        self.add(o_b_dist)

        self.wait(2)
        self.play(FadeOut(given, diametr_gr, radius_gr, o_b_dist), run_time=2)

        # # part 7
        self.play(Create(auxiliary_dots))
        self.play(Create(dashed_line_d_p), run_time=2)
        self.play(Create(dashed_line_c_f), run_time=2)
        self.play(Create(left_triangle), run_time=2)
        self.play(Create(right_triangle), run_time=2)
        l_r_triangles = VGroup(left_triangle, right_triangle)
        self.play(Indicate(l_r_triangles), run_time=2)
        self.play(
            Transform(left_triangle, similar[0][0:4]), run_time=2)
        self.play(Create(similar[0][4]))
        self.play(
            Transform(right_triangle, similar[0][5:9]), run_time=2)
        self.play(
            Transform(similar.copy(), similar_f), run_time=2)

        # Part 8
        self.play(Create(brace_x), run_time=2)
        self.play(
            Transform(brace_x, x_text), run_time=2)

        # Part 9
        self.play(Create(brace_y), run_time=2)
        self.play(
            Transform(brace_y, y_text), run_time=2)

        # Part 10
        # left
        self.play(Create(b_p_brace), run_time=2)
        self.play(
            Transform(b_p_brace, b_p), run_time=2)

        # right
        self.play(Create(b_f_brace), run_time=2)
        self.play(
            Transform(b_f_brace, b_f), run_time=2)

        # formula \frac{x-2}{y}= \frac{y}{x+2}
        self.play(Write(rightarrow), run_time=2)
        self.play(
            Transform(b_p[0][3:6].copy(), formula_simulate[0][0:4]), run_time=2)
        self.play(
            Transform(y_text_1.copy(), formula_simulate[0][4]), run_time=2)
        self.play(Write(formula_simulate[0][5]), run_time=2)
        self.play(
            Transform(y_text_2.copy(), formula_simulate[0][6:8]), run_time=2)
        self.play(
            Transform(b_f[0][3:6].copy(), formula_simulate[0][8:11]), run_time=2)

        # formula y^{2}=\left ( x-2 \right )\left ( x+2 \right )
        y_gr = VGroup(formula_simulate[0][4], formula_simulate[0][6])
        self.play(
            Transform(y_gr.copy(), formula_y[0][0:2]), run_time=2)
        self.play(Write(formula_y[0][2]), run_time=2)
        x_gr = VGroup(formula_simulate[0][0:3], formula_simulate[0][9:12])
        self.play(
            Transform(x_gr.copy(), formula_y[0][3:13]), run_time=2)
        self.play(Write(identity_under), run_time=2)
        self.play(Write(y_square[0][0:3]), run_time=2)
        self.play(Indicate(identity_under), run_time=2)
        self.play(Indicate(formula_y[0][3:13]), run_time=2)
        self.play(
            Transform(formula_y[0][3:13].copy(), y_square[0][3:13]), run_time=2)
        self.play(Create(y_square_surround), run_time=2)

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
