######################
### Map with label ###
######################

#PACKAGES
library(geobr)
library(ggrepel)
library(ggplot2)

#Loading .shp (capital = Aracaju, state = Sergipe, country = Brasil)
se = read_state(code_state = 'SE') #reading information from IBGE
aju = data.frame(lon = -37.0748, lat = -10.9095, municipio = 'Aracaju') 
#create data frame with information of capital

#plot map
ggplot(se)+ #set dataset
  geom_sf(fill='#74b9ff')+ #set pallete
  geom_point(data = aju, aes(x=lon, y=lat), size=2,pch=20)+ #set point in the map
  geom_label_repel(data = aju, aes(x=lon, y=lat, label = municipio))+ #plot label
  theme_void()+labs(x=NULL,y=NULL)
