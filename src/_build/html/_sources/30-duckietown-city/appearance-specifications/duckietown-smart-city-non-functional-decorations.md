```{seo}
:description: Enhance your Duckietown with non-functional decorations and learn best practices for creating a vibrant but well specified robotics environment.
:keywords: Duckietown, decorations, non-functional layer, robotics, Duckiebots, colored felts, modular cities, robotics education, creative design, appearance specifications
```


(dt-ops-non-functional-layer)=
# Decorations

Non-functional objects, such as decorative buildings, are placed on the floor layer of empty tiles in Duckietown. These objects are considered non-functional when used solely for decorative purposes.

The citizens of Duckietown appreciate vibrant, visually appealing cities and encourage creative efforts to enhance the empty spaces with decorations.

## Ideas for Decorative Enhancements

- **Colored Felts**: Simulate grass, water, or other natural elements to add realism to the environment.
- **Custom Contraptions**: Any imaginative addition that beautifies the city and pleases its citizens is welcome.

```{caution}
1. Ensure that decorations do not interfere with the tilemap and signals layers.
2. Avoid using colors that Duckiebots interpret, such as red, yellow, and white.
3. Use non-reflective materials to prevent algorithm debugging issues caused by glare.
```

## Background Considerations

Even though Duckiebot drivers are trained to focus on the road, the **background** (e.g., walls or furniture in the room where Duckietown is assembled) also plays a role in the overall experience. A thoughtfully designed environment enhances both aesthetics and functionality.
