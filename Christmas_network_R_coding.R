library(igraph)
data <- read.csv("Christmas_network.csv", header=T)
y <- data.frame(data$source, data$target, data$width)
net <- graph.data.frame(y, directed=T)
coords <- layout_in_circle(net)

plot(net,
     vertex.color = 'red',
     vertext.size = 3,
     edge.arrow.size = 0.1,
     vertex.label.cex = 0.8,
     layout = coords, edge.width=edge.betweenness(net))