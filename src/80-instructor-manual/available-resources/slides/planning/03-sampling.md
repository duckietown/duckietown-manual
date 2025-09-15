(slides-and-recordings-planning-sampling)=
# Sampling-based Planning

```{seo}
:description: Sampling-based planning in Duckietown 
:keywords: sampling-based planning, RRT, PRMs
```

In the [previous section](slides-and-recordings-planning-graphs), we introduced how graphs can be searched. In this section, we discuss practical, and very commonly used strategies for building these graphs. 

Since, in general, the configuration space is large and potentially high dimensional, we do not want to search it exhaustively. Instead, it turns out that we can use strategies to sample it and then construct a graph whose edges constitute collision-free paths. 


```{slides} ../../../../_assets/instructor-manual/planning-sampling-based.pdf
```



