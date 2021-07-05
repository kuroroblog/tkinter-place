import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # width : 幅を設定
        # height : 高さを設定
        # borderwidth : 枠の大きさを設定
        # bg : 背景色を設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # relief : 枠のデザインを設定する。
        # reliefについて : https://cercopes-z.com/Python/stdlib-tkinter-widget-frame-py.html#detail-relief
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master, width=400, height=400, borderwidth=20, bg="green", relief=tk.SUNKEN)

        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか？
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame, text="label", width=30, height=15, bg="blue")

        # frame Widget(Frame)を親要素とした場合に、label Widgetをどのように配置するのか?
        label.place(x=0, y=0)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
