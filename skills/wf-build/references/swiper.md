# Swiper

[Swiper](https://swiperjs.com/) is a slider library loaded as one stylesheet and one script. Reach for it when a section needs a slider or carousel the native Slider cannot give: slides from a Collection List, several slides in view, slides of their own width, free dragging, a continuous loop, or settings that change with screen width.

Propose it in the brief, naming the behavior it adds, because it loads a script on the site. Take the include tags from Swiper's [get started](https://swiperjs.com/get-started) page and pin the major version it shows. Where the site already loads Swiper, use that version.

## Structure

Swiper needs three nested elements carrying its own class names, beside the site's classes:

```text
swiper                 the visible frame
  swiper-wrapper       the moving track
    swiper-slide       one slide, repeated
```

For a Collection List, the Collection List Wrapper is `swiper`, the Collection List is `swiper-wrapper`, and each Collection Item is `swiper-slide`.

Keep arrows, pagination and the scrollbar inside the same component root as the frame, each on a class from the site's grammar, and pass those elements to Swiper in the script.

## Styling

Swiper's classes carry Swiper's own CSS, so leave them unstyled. Put size, spacing and look on the site's classes on the same elements. Give the frame a width, and a height where slides do not set one. Set the gap between slides with Swiper's `spaceBetween` setting, since a margin or gap on the track breaks its position math.

The Designer canvas runs no site scripts, so slides sit in a row or a stack there. Check the slider in Preview or on staging.

## Script

Write one script that starts every slider of that kind on the page, each scoped to its own root:

```js
document.querySelectorAll(".testimonials_component").forEach((root) => {
  new Swiper(root.querySelector(".swiper"), {
    slidesPerView: "auto",
    spaceBetween: 24,
    navigation: {
      prevEl: root.querySelector(".testimonials_arrow.is-prev"),
      nextEl: root.querySelector(".testimonials_arrow.is-next"),
    },
  });
});
```

Put the script where the grammar file says custom code goes. Read each setting's entry in the [Swiper API](https://swiperjs.com/swiper-api) before using it. `loop` needs more slides than are in view, and `slidesPerView: "auto"` needs a width on each slide.
