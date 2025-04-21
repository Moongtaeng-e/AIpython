import tkinter as tk
from PIL import Image, ImageTk

def show_image(image_path):
    try:
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference!
    except Exception as e:
        print(f"오류 발생: {e}")
        tk.messagebox.showerror("오류", f"이미지 파일을 열 수 없습니다: {e}")

# 메인 윈도우 생성
window = tk.Tk()
window.title("동물 이미지 뷰어")

# 이미지 라벨 생성
image_label = tk.Label(window)
image_label.pack(padx=10, pady=10)

# 강아지 버튼 생성
dog_button = tk.Button(window, text="강아지", command=lambda: show_image("dog.jpg"))
dog_button.pack(pady=5)

# 고양이 버튼 생성
cat_button = tk.Button(window, text="고양이", command=lambda: show_image("cat.jpg"))
cat_button.pack(pady=5)

# 토끼 버튼 생성
rabbit_button = tk.Button(window, text="토끼", command=lambda: show_image("rabbit.jpg"))
rabbit_button.pack(pady=5)

# 메인 루프 실행
window.mainloop()