import streamlit as st
import time
import numpy as np
import pandas as pd
from PIL import Image

st.title('Hello world.')

st.write('Progressbar')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.01)

'Done!!'

st.write('Display Image')

hobby = st.sidebar.text_input('Tell me your hobby')
'Your hobby is ', hobby, '.'

condition = st.sidebar.slider('How is your current spirit?', 0, 100, 50)
'Your current spirit is ', condition, '.'

if st.checkbox('Show Image'):
  img = Image.open('zona_sample.001.jpeg')
  st.image(img, caption='zona', width=200)#, use_column_width=True)

option = st.selectbox('Tell me the number you like.',
  list(range(1,11))
)
'The number you like is ', option, '.'

st.write('DataFrame')

df = pd.DataFrame({
  'L1': [ 1, 2, 3, 4 ],
  'L2': [ 10, 20, 30, 40 ],
  'L3': [ 400, 300, 200, 100 ],
})

st.write(df)
st.dataframe(df, width=1000, height=1000)
st.table(df.style.highlight_max(color='red',axis=0))


"""
# Chapter
## Clause
### Section


```python
import streamlit as st
import numpy as np
import pandas as pd

"""
"""
```C++
#include <string.h>

using namespace std;

int main() {
  return 0;
}
"""

df = pd.DataFrame(
  np.random.rand(20, 3),
  columns=['a','b','c']
)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)


df = pd.DataFrame(
  np.random.rand(100, 2)/(50,50) + [ 35.69, 139.70 ],
  columns=['lat', 'lon' ]
)
st.map(df)



st.balloons()

st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')

col1, col2, col3 = st.beta_columns(3)

with col1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")

if st.button('Say hello'):
  st.write('Why hello there')
else:
  st.write('Goodbye')

number = st.number_input('Insert a number')
st.write('The current number is ', number)

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

video_file = open('sample-5s.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)


expander1 = st.beta_expander('Question1')
expander1.write('Answer1')

expander2 = st.beta_expander('Question2')
expander2.write('Answer2')

expander3 = st.beta_expander('Question3')
expander3.write('Answer3')
