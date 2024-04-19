#!/usr/bin/env python
# coding: utf-8

# In[1]:


import schemdraw


# In[2]:


from schemdraw import flow


# In[3]:


with schemdraw.Drawing() as d:
    
    drawing_size = (300, 300)
    
    d.config(fontsize=18)
    b = flow.Start().label('START')
    
    flow.Arrow().down(d.unit/4)
    d1 = flow.Decision(w=5, h=3.9, E='NO', S='YES').label('Is the source\n from 01.01.2019\n onwards?')
    
    flow.Arrow().length(d.unit/4)
    d2 = flow.Decision(w=5, h=3.9, E='NO', S='YES').label('Is the source\n the direct\n provider?')
    
    flow.Arrow().length(d.unit/4)
    d3 = flow.Decision(w=5, h=3.9, E='NO', S='YES').label('Does the \n source provide\n an exact\n number?')
    
    flow.Arrow().right(d.unit*1).at(d1.E)
    s1 = flow.Box(w=2, h=1).anchor('W').label('25%')
    
    flow.Arrow().right(d.unit*0.5).at(d2.E)
    d4 = flow.Decision(w=5, h=3.9, E='NO', S='YES').label('Is the source\n correctly cited?')
                                                
    flow.Arrow().right(d.unit*0.5).at(d4.E)
    s2 = flow.Box(w=2, h=1).anchor('W').label('50%')
    
    flow.Arrow().right(d.unit*1).at(d3.E)
    s4 = flow.Box(w=2, h=1).anchor('W').label('75%')
    
    flow.Wire('-|', arrow='->').at(d4.S).to(s4.N)
    
    flow.Arrow().down(d.unit/4).at(d3.S)
    listen = flow.Box(w=2, h=1).label('100%')


# The flow chart is used to provide a score for the credibility of the sources used. Best efforts are used to find a source of 100%, however in some cases the only information available comes from a lower % source.
# 
# An average % will be found for reliability across finance, employment, and benefits sources.
# 
# The % for the sources will not be combined with overall score, but instead will be mentioned alongside overall score to quantify reliability of source.
