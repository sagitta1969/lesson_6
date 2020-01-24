class Stationery:
    def __init__(self, title='something that can draw'):
        self.title = title

    def draw(self):
        print(f"just start drawing! {self.title}")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print(f"start drawing with {self.title} pen!")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print(f"start drawing with {self.title} pencil!")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        print(f"start drawing with {self.title} handle!")

stat = Stationery()
stat.draw()
pen = Pen("Perker")
pen.draw()
Pencil = Pencil("Faber-Castel")
Pencil.draw()
handle = Handle("COPIC")
handle.draw()