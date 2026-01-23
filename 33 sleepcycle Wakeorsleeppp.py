import ipywidgets as widgets
from IPython.display import display, HTML

# 1. สร้างสไตล์ CSS สำหรับสีพาสเทล
style = """
<style>
    .main-box {
        background-color: #FADADD; /* ชมพูพาสเทล */
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #B2F2BB; /* ขอบเขียวมิ้นต์ */
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    .result-box {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 10px;
        margin-top: 15px;
        color: #555;
        font-weight: bold;
    }
    .calc-button {
        background-color: #B2F2BB !important; /* เขียวมิ้นต์ */
        color: #3D3D3D !important;
        font-weight: bold !important;
        border-radius: 8px !important;
    }
</style>
"""
display(HTML(style))

# 2. สร้าง Widgets
title = widgets.HTML("<h2>🌙 Wake or Sleep by Pammy ☀️</h2>")

choice = widgets.Dropdown(
    options=[('คำนวณเวลาตื่น (ใส่เวลานอน)', 1), ('คำนวณเวลานอน (ใส่เวลาตื่น)', 2)],
    value=1,
    description='เลือกโหมด:',
    style={'description_width': 'initial'}
)

time_input = widgets.Text(
    value='22:30',
    placeholder='HH:MM',
    description='กรอกเวลา:',
    style={'description_width': 'initial'}
)

button = widgets.Button(
    description='คำนวณเลย!',
    button_style='', # สไตล์จะถูกคุมด้วย CSS คลาสข้างบน
)
button.add_class("calc-button")

output = widgets.Output()

# 3. ฟังก์ชันคำนวณ
def on_button_clicked(b):
    with output:
        output.clear_output()
        try:
            raw_time = time_input.value
            hours, minutes = map(int, raw_time.split(':'))
            total_minutes = (hours * 60) + minutes
            
            results = []
            for i in range(4, 7):
                cycle_time = i * 90
                if choice.value == 1:
                    res_min = (total_minutes + cycle_time + 15) % 1440
                    text = f"รอบที่ {i} (นอน {i*1.5} ชม.)"
                else:
                    res_min = (total_minutes - cycle_time) % 1440
                    text = f"รอบที่ {i} (นอน {i*1.5} ชม.)"
                
                res_h = int(res_min // 60)
                res_m = int(res_min % 60)
                results.append(f"<b>{text}:</b> {res_h:02d}:{res_m:02d} น.")
            
            res_html = "<div class='result-box'>" + "<br>".join(results) + "</div>"
            display(HTML(res_html))
            
        except Exception:
            display(HTML("<p style='color:red;'>กรุณาใส่เวลาในรูปแบบ HH:MM เช่น 23:00</p>"))

button.on_click(on_button_clicked)

# 4. จัด Layout และแสดงผล
ui = widgets.VBox([title, choice, time_input, button, output])
ui.add_class("main-box")
display(ui)
