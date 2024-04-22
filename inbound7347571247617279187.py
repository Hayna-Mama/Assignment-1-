#1
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return x**2 - 10
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.grid(True, color='blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph of x^2 - 10")
plt.axhline(y=0, color="red")
plt.axvline(x=0, color="red")
plt.show()

#2
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return x**3 + x - 100
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.grid(True, color='blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph of x^3 + x - 10")
plt.axhline(y=0, color="red")
plt.axvline(x=0, color="red")
plt.show()

#3
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return x**10 - x**8 -x**2 - 8
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.grid(True, color='blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph of x^10 - x^8 -x^2 - 8")
plt.axhline(y=0, color="red")
plt.axvline(x=0, color="red")
plt.show()

#4
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return x**4 + x**3 + x**2 + x +1 
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.grid(True, color='blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph of x^4 + x^3 + x^2 + x + 1")
plt.axhline(y=0, color="red")
plt.axvline(x=0, color="red")
plt.show()

#5
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return (x**2 + x + 10)/(2*x)
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.grid(True, color='blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph of (x^2 + x + 10)/2x")
plt.axhline(y=0, color="red")
plt.axvline(x=0, color="red")
plt.show()

#6
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return np.sin(x)/(3*x)
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.grid(True, color='blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph of sinx/3x")
plt.axhline(y=0, color="red")
plt.axvline(x=0, color="red")
plt.show()

#7
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return x**3 + (2*x**2) - (10*x) +3
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.grid(True, color='blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph of x^3+2x^2-10x+3")
plt.axhline(y=0, color="red")
plt.axvline(x=0, color="red")
plt.show()

#8
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return np.cos(x)/(5*x)
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.grid(True, color='blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph of cosx/5x")
plt.axhline(y=0, color="red")
plt.axvline(x=0, color="red")
plt.show()

#9
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return ((x**3)/(2*x))-(10*x)
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.grid(True, color='blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph of (x^3/2x)-10x")
plt.axhline(y=0, color="red")
plt.axvline(x=0, color="red")
plt.show()

#10
import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return (x+2)*(x+3)*(x-4)
x = np.linspace(-5, 5, 100)  
y = f(x)
plt.plot(x, y)
plt.grid(True, color='blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph of f(x)=(x+2)(x+3)(x-4)")
plt.axhline(y=0, color="red")
plt.axvline(x=0, color="red")
plt.show()