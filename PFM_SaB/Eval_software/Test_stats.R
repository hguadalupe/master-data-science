library(ggplot2)

#EMEPLO
library(gapminder)
gapminder
?gapminder
summary(gapminder)
library(tidyverse)
glimpse(gapminder)

dim(gapminder)

View(gapminder)


ggplot(gapminder, aes(x = gdpPercap, y = lifeExp))

ggplot(gapminder, aes(x = gdpPercap, y = lifeExp)) + geom_point()

ggplot(gapminder, aes(x = gdpPercap, y = lifeExp)) + geom_point() + scale_x_log10()

ggplot(gapminder, aes(x = gdpPercap, y = lifeExp)) + geom_point() + scale_x_log10() + geom_point(aes(color=continent)) 

ggplot(gapminder, aes(x = gdpPercap, y = lifeExp)) + geom_point() + scale_x_log10() + geom_point(aes(color=continent)) + geom_smooth()

ggplot(gapminder, aes(x = gdpPercap, y = lifeExp)) + geom_point() + scale_x_log10() + geom_point(aes(color=continent)) + geom_smooth(lwd=1, se=FALSE, method="lm", col="black")

ggplot(gapminder, aes(x = gdpPercap, y = lifeExp, color = continent))  + geom_point() + scale_x_log10()  + geom_smooth(se=F, lwd=1)



rang_notas<- seq(1,5,1)
rang_expe<- seq(1,10,1)
rang_softs<- c("Revit","Aecosim","ALLPLAN","Archicad")

notas_re<- sample(rang_notas,1000,replace=TRUE,prob = c(1,1,7,10,8))
notas_ae<- sample(rang_notas,30,replace=TRUE,prob = c(1,2,2,1,0))
notas_al<- sample(rang_notas,70,replace=TRUE,prob = c(1,3,3,2,1))
notas_ar<- sample(rang_notas,400,replace=TRUE,prob = c(1,2,4,2,4))
notas_tot<- c(notas_ae,notas_ar,notas_al,notas_re)

exp_re <- sample(rang_expe,1000,replace=TRUE,prob = c(3,7,5,4,2,3,2,1,2,1))
exp_ae <- sample(rang_expe,30,replace=TRUE,prob = c(1,2,3,2,2,3,1,0,0,0))
exp_al <- sample(rang_expe,70,replace=TRUE,prob = c(0,1,3,4,2,3,2,3,0,0))
exp_ar <- sample(rang_expe,400,replace=TRUE,prob = c(2,2,3,4,4,3,4,2,1,0))
exp_tot <- c(exp_ae,exp_ar,exp_al,exp_re)

soft_tot <- c(rep("Aecosim",30),rep("Archicad",400),rep("ALLPLAN",70),rep("Revit",1000))

eval_soft <- data.frame(notas_tot,exp_tot,soft_tot)



ggplot(eval_soft, aes(x = exp_tot, y = notas_tot, color = soft_tot))  + geom_point() + geom_smooth(se=F, lwd=1,method = "loess") + geom_jitter(alpha = 1/3)

# Ahora vamos a hacer elgráfico de softwares predominantes:

notas_predom<- c(notas_ar,notas_re)
exp_predom <- c(exp_ar,exp_re)
soft_predom <- c(rep("Archicad",400),rep("Revit",1000))
eval_predom_soft <- data.frame(notas_predom,exp_predom,soft_predom)
ggplot(eval_predom_soft, aes(x = exp_predom, y = notas_predom, color = soft_predom))  + geom_point() + geom_smooth(se=F, lwd=1,method = "loess") + geom_jitter(alpha = 1/4)

