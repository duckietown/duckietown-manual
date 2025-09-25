```{seo}
:description: Learn how to incorporate experimental street name signs into Duckietown, for enhanced aesthetics and outreach.
:keywords: Duckietown, street name signs, non-functional elements, robotics, autonomous robots, road signs, Duckiebots, traffic signs, robotics outreach, modular cities
```

(specs-layer-street-names)=
# Traffic Signs - Street Name Signs

```{attention}
The traffic sign type described here is experimental. Use at your own risk!
```

Street name signs are **non-functional** elements, meaning they are not integrated into any Duckiebot behavior. However, they add an aesthetic and outreach element to Duckietown, making the city more engaging and visually appealing.

```{tip}
Consider naming the main avenue in your Duckietown after someone significant in your community, like your Department Head or a local robotics advocate.
```

## Specifications

- **Font**: Arial.
- **Alphabet**: English uppercase. Different writing systems may require adjusted algorithms.
- **Color**: White foreground and green background.
- **Border**: No additional borders.
- **Width**:
  - 4.5 in for ID 500-511.
  - **6.1 in +1.1 in "ST"** or **5.5 in +1.7 in "AVE"**.
- **Text direction**: Horizontal for alphabetical languages.

### Placement Guidelines

- Street name signs must be placed **outside the allowable driving region** and should be visible from both sides of the road.
- If street name signs are used, every road segment should have at least one sign.
- **Turn tiles** must include a road name sign.
- Placement should follow the guidelines shown in {numref}`fig:name-placement`.

````{list-table} Placement of Road Name Signs
:name: fig:name-placement

* - ```{figure} ../../_images/duckietown-city/appearance_specifications/tiles/name-signs-turn.svg
    :name: subfig:name-signs-turn

    Turn
    ```

  - ```{figure} ../../_images/duckietown-city/appearance_specifications/tiles/name-signs-straight.svg
    :name: subfig:name-signs-straight

    Straight
    ```
````

Street name signs should never be placed perpendicular to the road, as they can obstruct the driving region due to their size.