
/*
키보드로 입력할 수 없는 다음 모양을 출력해보자.
(** 참고 : 운영체제의 문자 시스템에 따라 아래와 같은 모양이 출력되지 않을 수 있다.)

┌┬┐
├┼┤
└┴┘
*/

public class Main {

	public static void main(String[] args) {
		System.out.printf("\u250c\u252c\u2510\n\u251c\u253c\u2524\n\u2514\u2534\u2518");
	}

}
