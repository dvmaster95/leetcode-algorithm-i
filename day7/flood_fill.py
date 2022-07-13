image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

def floodFill(image, sr, sc, color):

    def horizontal_fill(image, rows, column, color):
        mod_cols = []
        for row in rows:
            # forward
            pivot = column
            while pivot < len(image[row][:]):
                if image[row][pivot] > 0 and image[row][pivot] != color:
                    image[row][pivot] = color
                    mod_cols.append(pivot)
                pivot += 1
            # backwards
            pivot = column
            while pivot >= 0:
                if image[row][pivot] > 0 and image[row][pivot] != color:
                    image[row][pivot] = color
                    mod_cols.append(pivot)
                pivot -= 1
    
    def vertical_fill(image, rows, column, color):
        mod_cols = []
        for row in rows:
            # forward
            pivot = column
            while pivot < len(image[row][:]):
                if image[row][pivot] > 0 and image[row][pivot] != color:
                    image[row][pivot] = color
                    mod_cols.append(pivot)
                pivot += 1
            # backwards
            pivot = column
            while pivot >= 0:
                if image[row][pivot] > 0 and image[row][pivot] != color:
                    image[row][pivot] = color
                    mod_cols.append(pivot)
                pivot -= 1
        
    horizontal_fill(image, [sr], sc, color)


floodFill(image, sr, sc, color)