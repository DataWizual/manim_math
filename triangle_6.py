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

        y_square_s = self.texts(MathTex, r"y^{2}= x^{2}-4",
                                None, None, 4.5, 3, None, True, 0.5)
        y_square_s[0][0].set_color(YELLOW)
        y_square_s[0][3].set_color(YELLOW)
        y_square_s[0][6].set_color(BLUE)
        y_square_s_surround = SurroundingRectangle(y_square_s, color='#ff00ff')
        y_2 = VGroup(y_square_s, y_square_s_surround)

        x_y_r_8 = self.texts(MathTex, r"x= \sqrt{34}",
                             None, y_2, None, None, DOWN, False, 0.5)
        x_y_r_8[0][0].set_color(YELLOW)
        x_y_r_8[0][4:6].set_color(BLUE)
        x_y_r_8_surround = SurroundingRectangle(x_y_r_8, color='#ff00ff')

        x_gr = VGroup(x_y_r_8, x_y_r_8_surround)
        x_gr.align_to(y_2, LEFT)

        # Part 18 On this equation
        # y^2=x^2-4
        y_find = self.texts(MathTex, r"y^{2}= x^{2}-4",
                            None, None, 1, 2, None, True, 0.5)
        y_find[0][0].set_color(YELLOW)
        y_find[0][3].set_color(YELLOW)
        y_find[0][6].set_color(BLUE)

        # Part 19 we will to substitute x value by square root of 34
        # y^2=(√34)^2-4
        # func, text, color, nextto, x, y, side, choice, buff
        y_find_1 = self.texts(MathTex, r"y^{2}=\left ( \sqrt{34} \right )^{2}-4",
                              None, y_find, None, None, DOWN, False, 0.5)
        y_find_1[0][0].set_color(YELLOW)
        y_find_1[0][6:8].set_color(BLUE)
        y_find_1[0][11].set_color(BLUE)
        y_find_1.align_to(y_find, LEFT)

        # Part 20 Therefore, y square to be equal to 30
        # y^2=30
        y_find_2 = self.texts(MathTex, r"y^{2}=34-4",
                              None, y_find_1, None, None, DOWN, False, 0.5)
        y_find_2[0][0].set_color(YELLOW)
        y_find_2[0][3:5].set_color(BLUE)
        y_find_2[0][6].set_color(BLUE)
        y_find_2.align_to(y_find, LEFT)

        y_find_6 = self.texts(MathTex, r"y= \sqrt{30}",
                              None, x_gr, None, None, DOWN, False, 0.5)
        y_find_6[0][0].set_color(YELLOW)
        y_find_6[0][4:6].set_color(BLUE)
        y_find_6.align_to(x_y_r_8, LEFT)
        y_find_surround_1 = SurroundingRectangle(y_find_6, color='#ff00ff')

        y_find_6_gr = VGroup(y_find_6, y_find_surround_1)

        rect_text = self.texts(MathTex, r"S_{r}=DPFC",
                               None, None, 0.5, 2.0, None, True, None)
        rect_text[0][0:2].set_color(YELLOW)
        rect_text[0][3:7].set_color('#00ff00')

        # Part 24 in our case the area of this rectangle will be S(rect)=2xy
        rect_area = self.texts(MathTex, r"S_{r}=2xy",
                               None, rect_text, None, None, DOWN, False, 0.5)
        rect_area[0][0:2].set_color(YELLOW)
        rect_area[0][3].set_color(BLUE)
        rect_area[0][4:6].set_color(YELLOW)
        rect_area.align_to(rect_text, LEFT)

        # Part 25 Taking into account the values of x and y, we replace them
        # S(rect)=2√34 √30
        rect_area_1 = self.texts(MathTex, r"S_{r}=2\sqrt{34}\sqrt{30}",
                                 None, rect_area, None, None, DOWN, False, 0.5)
        rect_area_1[0][0:2].set_color(YELLOW)
        rect_area_1[0][3].set_color(BLUE)
        rect_area_1[0][6:8].set_color(BLUE)
        rect_area_1[0][10:12].set_color(BLUE)
        rect_area_1.align_to(rect_text, LEFT)

        # Part 26 and if we simplify everything, the area of this rectangle will be equal
        # S(rect)= 2√(2*17) √(2*15) S_{r}=2\sqrt{2*17}*\sqrt{2*15}
        rect_area_2 = self.texts(MathTex, r"S_{r}=2\sqrt{2*17}\sqrt{2*15}",
                                 None, rect_area_1, None, None, DOWN, False, 0.5)
        rect_area_2[0][0:2].set_color(YELLOW)
        rect_area_2[0][3].set_color(BLUE)
        rect_area_2[0][6].set_color(BLUE)
        rect_area_2[0][8:10].set_color(BLUE)
        rect_area_2[0][13].set_color(BLUE)
        rect_area_2[0][15:17].set_color(BLUE)
        rect_area_2.align_to(rect_text, LEFT)

        # S(rect)=2*2√(17⋅15)
        rect_area_3 = self.texts(MathTex, r"S_{r}=2*2\sqrt{17*15}",
                                 None, rect_area_2, None, None, DOWN, False, 0.5)
        rect_area_3[0][0:2].set_color(YELLOW)
        rect_area_3[0][3].set_color(BLUE)
        rect_area_3[0][5].set_color(BLUE)
        rect_area_3[0][8:10].set_color(BLUE)
        rect_area_3[0][11:13].set_color(BLUE)
        rect_area_3.align_to(rect_text, LEFT)

        # S(rect)=4√255
        rect_area_4 = self.texts(MathTex, r"S_{r}=4\sqrt{255}",
                                 None, rect_area_3, None, None, DOWN, False, 0.5)
        rect_area_4[0][0:2].set_color(YELLOW)
        rect_area_4[0][3].set_color(BLUE)
        rect_area_4[0][6:9].set_color(BLUE)
        rect_area_4.align_to(rect_text, LEFT)
        rect_area_4_surround = SurroundingRectangle(
            rect_area_4, color='#ff00ff')
        rect_area_gr = VGroup(rect_area_4, rect_area_4_surround)

        rect_area_5 = self.texts(MathTex, r"S_{r}=4\sqrt{255}",
                                 None, None, 4.5, 3.0, None, True, 0.5)
        rect_area_5[0][0:2].set_color(YELLOW)
        rect_area_5[0][3].set_color(BLUE)
        rect_area_5[0][6:9].set_color(BLUE)
        rect_area_5.align_to(y_find_6, LEFT)
        rect_area_5_surround = SurroundingRectangle(
            rect_area_5, color='#ff00ff')
        rect_area_gr_1 = VGroup(rect_area_5, rect_area_5_surround)

        # Now let's focus on the blue rectangle
        triangle_1 = self.lines(
            b_triangle_dot, d_triangle_dot, '#0000ff', Line, True)
        triangle_2 = self.lines(
            d_triangle_dot, c_triangle_dot, '#0000ff', Line, True)
        triangle_3 = self.lines(
            c_triangle_dot, b_triangle_dot, '#0000ff', Line, True)
        triangle_gr = VGroup(triangle_1, triangle_2, triangle_3)
        # Here you can see that its base is equal to the side of the rectangle,
        # which is equal to 2x and the height is equal y
        brace_2x, brace_2x_text = self.braces(
            Line(d_triangle_dot, c_triangle_dot), r"2x", True, None)
        brace_2x_gr = VGroup(brace_2x, brace_2x_text)

        brace_y, brace_y_text = self.braces(
            Line(p_dot, d_triangle_dot), r"y", False, PI / 2)
        y_gr = VGroup(brace_y, brace_y_text)

        # We conclude that the area of the triangle will be equal to half of this rectangle
        # S(triangle)=1/2* S(rect)
        triangle_text = self.texts(MathTex, r"S_{t}=\frac{1}{2}S_{r}",
                                   None, None, 0, 2.0, None, True, None)
        triangle_text[0][0:2].set_color(YELLOW)
        triangle_text[0][3].set_color(BLUE)
        triangle_text[0][5].set_color(BLUE)
        triangle_text[0][6:7].set_color(YELLOW)

        # S(triangle)=1/2 4√255
        # func, text, color, nextto, x, y, side, choice, buff
        triangle_text_1 = self.texts(MathTex, r"S_{t}=\frac{1}{2}*4\sqrt{255}",
                                     None, triangle_text, None, None, DOWN, False, 0.5)
        triangle_text_1[0][0:2].set_color(YELLOW)
        triangle_text_1[0][3].set_color(BLUE)
        triangle_text_1[0][5].set_color(BLUE)
        triangle_text_1[0][7].set_color(BLUE)
        triangle_text_1[0][10:13].set_color(BLUE)
        triangle_text_1.align_to(triangle_text, LEFT)

        # S(triangle)=2√255
        triangle_text_2 = self.texts(MathTex, r"S_{t}=2\sqrt{255}",
                                     None, triangle_text_1, None, None, DOWN, False, 0.5)
        triangle_text_2[0][0:2].set_color(YELLOW)
        triangle_text_2[0][3].set_color(BLUE)
        triangle_text_2[0][6:9].set_color(BLUE)
        triangle_text_2.align_to(triangle_text, LEFT)

        # As a result, the area of the blue right triangle will be
        # approximately equal to 32 square units
        triangle_text_3 = self.texts(MathTex, r"S_{t}=31.937\approx 32 sq.units",
                                     None, triangle_text_2, None, None, DOWN, False, 0.5)
        triangle_text_3[0][0:2].set_color(YELLOW)
        triangle_text_3[0][3:5].set_color(BLUE)
        triangle_text_3[0][6:9].set_color(BLUE)
        triangle_text_3[0][10:12].set_color(BLUE)
        triangle_text_3.align_to(triangle_text, LEFT)

        triangle_text_sur = SurroundingRectangle(
            triangle_text_3, color='#ff00ff')

        # part 1
        self.add(task_text_1)
        self.add(img)
        self.add(line_dot)
        self.add(verts)
        self.add(auxiliary_dots)
        self.add(dashed_line_d_p)
        self.add(dashed_line_c_f)
        self.add(x_text)
        self.add(y_text)
        self.add(y_2)
        # ***********************************
        self.add(x_gr)
        self.add(y_find_6_gr)
        self.add(rect_text)
        self.add(rect_area)
        self.add(rect_area_1)
        self.add(rect_area_2)
        self.add(rect_area_3)
        self.add(rect_area_gr)
        self.wait(2)
        self.play(FadeOut(y_2, x_gr, y_find_6_gr, rect_text,
                  rect_area, rect_area_1, rect_area_2, rect_area_3), run_time=3)
        self.wait(2)
        self.play(Transform(rect_area_gr, rect_area_gr_1), run_time=3)
        self.wait(2)
        self.play(FadeIn(triangle_gr), run_time=3)
        self.wait(2)
        self.play(Indicate(triangle_gr), run_time=3)
        self.wait(2)
        self.play(FadeOut(triangle_gr), run_time=3)
        self.play(FadeIn(brace_2x_gr), run_time=3)
        self.wait(2)
        self.play(FadeOut(brace_2x_gr), run_time=3)
        self.play(FadeIn(y_gr), run_time=3)
        self.wait(2)
        self.play(FadeOut(y_gr), run_time=3)
        self.wait(2)
        self.play(FadeIn(triangle_text), run_time=3)
        self.wait(2)
        self.play(Transform(triangle_text.copy(), triangle_text_1), run_time=3)
        self.wait(2)
        self.play(Transform(triangle_text_1.copy(),
                  triangle_text_2), run_time=3)
        self.wait(2)
        self.play(Transform(triangle_text_2.copy(),
                  triangle_text_3), run_time=3)
        self.wait(2)
        self.play(Create(triangle_text_sur), run_time=3)

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
