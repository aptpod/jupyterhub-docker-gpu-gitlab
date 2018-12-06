# module imports
__modules__ = (
    'scipy',
    'numpy',
    'pandas',
    'matplotlib.pyplot',
)
__standfor__ = {
    'scipy': 'sp',
    'numpy': 'np',
    'pandas': 'pd',
    'matplotlib.pyplot': 'plt',
}

for __module__ in __modules__:
    __execution__ = 'import %s as %s' % (__module__, __standfor__[__module__])
    print(__execution__)
    exec(__execution__)

# plot inlining
__inline__ = 'matplotlib inline'
__gui__ = 'matplotlib auto'

try:
    get_ipython().magic(__inline__)
    print('%' + __inline__)

except:
    get_ipython().magic(__gui__)
    print('%' + __gui__)
    print("If you'd like to use `plt.show()` command,")
    print('you can type `plt.ioff()`/`plt.ion()` to turn interactive mode off/on.')

