#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

path= open('Netflix Christmas Cinematic Universe/Christmas_network - Sheet4.csv','r')
df=  pd.read_csv(path)
df[['source','target','width','label']]
G = nx.from_pandas_edgelist(df, 'source','target', edge_attr=['width','label'])
#img=plt.imread('/Users/alexesmerritt/Desktop/Netflix Christmas Cinematic Universe/img.jpg')
img4=mpimg.imread('Netflix Christmas Cinematic Universe/img4.jpg')
img5=mpimg.imread('Netflix Christmas Cinematic Universe/img5.jpg')
img6=mpimg.imread('Netflix Christmas Cinematic Universe/img6.jpg')
img9=mpimg.imread('Netflix Christmas Cinematic Universe/img9.jpg')
img10=mpimg.imread('Netflix Christmas Cinematic Universe/img10.jpg')
img11=mpimg.imread('Netflix Christmas Cinematic Universe/img11.jpg')
img13=mpimg.imread('Netflix Christmas Cinematic Universe/img13.jpg')
img18=mpimg.imread('Netflix Christmas Cinematic Universe/img18.jpg')
img29=mpimg.imread('Netflix Christmas Cinematic Universe/img29.jpg')
img30=mpimg.imread('Netflix Christmas Cinematic Universe/img30.jpg')
img31=mpimg.imread('Netflix Christmas Cinematic Universe/img31.jpg')
img32=mpimg.imread('Netflix Christmas Cinematic Universe/img32.jpg')

widths=[i['width']*5 for i in dict(G.edges).values()]
#labels=[edge['label'] for edge in dict(G.edges).values()]
edges = G.edges()
colors = [G[u][v]['label'] for u,v in edges]

pos=nx.spring_layout(G, k=0.15, iterations=20)

fig=plt.figure(figsize= (500,500))
ax=plt.subplot(111)
ax.set_aspect('equal')

#nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.xlim(-1,1)
plt.ylim(-1,1)

trans=ax.transData.transform
trans2=fig.transFigure.inverted().transform

piesize=0.1# this is the image size
p2=piesize/2.0
##THE CHRISTMAS PRINCE 1
pairings = [(4,img4),(5,img5),(6,img6),(9,img9),(10,img10), 
            (11,img11), (13,img13),(18, img18),(29,img29),
            (30,img30),(31,img31),(32,img32)]
for i in pairings: 
    xx,yy=trans(pos[i[0]]) # figure coordinates
    xa,ya=trans2((xx,yy)) # axes coordinates
    a = plt.axes([xa-p2,ya-p2, piesize, piesize])
    a.set_aspect('equal')
    a.imshow(i[1])
    a.axis('off')

nx.draw_networkx_edges(G,pos,ax=ax, width=widths, edge_color=colors, label=True)
print(G.nodes())
centrality = nx.eigenvector_centrality(G)
print([(node,centrality[node]) for node in centrality])
print('The Christmas Pirnce 3 has the highest Eigenvector centrality')
plt.show()
plt.savefig('Netflix Christmas Cinematic Universe/network.png',dpi=1000)