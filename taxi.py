import time
import flet as ft


def main(page: ft.Page):
  page.title = "عداد التاكسي الذكي"
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.bgcolor = "#f5f5f5"
  page.window_width = 400
  page.window_height = 600

  # متغيرات البرنامج
  passenger_count = ft.Ref[ft.Text]()
  fare_text = ft.Ref[ft.Text]()
  timer_text = ft.Ref[ft.Text]()

  passengers = [0]
  fare_per_passenger = 30
  target_passengers = [10]
  target_hours = [8]
  elapsed_seconds = [0]
  is_running = [False]

  target_pass_input = ft.TextField(
      label="هدف الركاب", value="10", width=120, keyboard_type=ft.KeyboardType.NUMBER
  )
  target_hours_input = ft.TextField(
      label="ساعات الشيفت", value="8", width=120, keyboard_type=ft.KeyboardType.NUMBER
  )

  def update_ui():
    p_count = passengers[0]
    total_fare = p_count * fare_per_passenger
    lbl_pass.value = f"عدد الركاب: {p_count}"
    lbl_fare.value = f"إجمالي الحساب: {total_fare} جنيه"
    page.update()

  def increment(e):
    passengers[0] += 1
    update_ui()
    if passengers[0] >= target_passengers[0]:
      page.open(
          ft.SnackBar(
              ft.Text("خلاص أنت خلصت عدد الركاب المستهدف!"),
              bgcolor=ft.colors.GREEN,
          )
      )

  def decrement(e):
    if passengers[0] > 0:
      passengers[0] -= 1
      update_ui()

  def reset_counter(e):
    passengers[0] = 0
    elapsed_seconds[0] = 0
    is_running[0] = False
    update_ui()
    lbl_timer.value = "وقت الشيفت: 00:00:00"
    page.update()

  # عناصر الواجهة
  lbl_pass = ft.Text("عدد الركاب: 0", size=20, weight=ft.FontWeight.BOLD)
  lbl_fare = ft.Text(
      "إجمالي الحساب: 0 جنيه", size=20, weight=ft.FontWeight.BOLD, color="green"
  )
  lbl_timer = ft.Text("وقت الشيفت: 00:00:00", size=16, color="grey")

  # الأزرار الكبيرة المناسبة للمس
  btn_plus = ft.ElevatedButton(
      "➕ زود راكب",
      color="white",
      bgcolor="blue",
      width=150,
      height=50,
      on_click=increment,
  )
  btn_minus = ft.ElevatedButton(
      "➖ نقص راكب",
      color="white",
      bgcolor="orange",
      width=150,
      height=50,
      on_click=decrement,
  )
  btn_reset = ft.ElevatedButton(
      "🔄 تصفير العداد",
      color="white",
      bgcolor="red",
      width=310,
      height=45,
      on_click=reset_counter,
  )

  page.add(
      ft.Text("🚖 نظام إدارة شيفت التاكسي", size=22, weight=ft.FontWeight.BOLD),
      ft.Divider(),
      lbl_pass,
      lbl_fare,
      lbl_timer,
      ft.Divider(),
      ft.Row(
          [target_pass_input, target_hours_input],
          alignment=ft.MainAxisAlignment.CENTER,
      ),
      ft.Row([btn_plus, btn_minus], alignment=ft.MainAxisAlignment.CENTER),
      btn_reset,
  )


ft.app(target=main)