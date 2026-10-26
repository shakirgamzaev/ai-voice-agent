<script lang="ts">
    let {width, height}: {width: number, height: number} = $props()

    const housePath = $derived(
        `M0 0 L${width} 0 L${width} ${height} L${width*0.7} ${height} V${height*0.68} H${width*0.3} V${height} H0 Z`
    )

    // Windows are squares sized relative to width only
    const win = $derived(width * 0.15)

    // Two columns, centered horizontally: 12% + 12% gap + 12% = 36% wide → 32% margin each side
    const colX = $derived([0.32, 0.56].map((f) => width * f))
    // Two rows in the upper wall, above the door (door top is at 0.68h).
    // Row offset = window + gap = 0.24w, so vertical spacing matches horizontal.
    const rowY = $derived([height * 0.15, height * 0.15 + width * 0.24])

    const windows = $derived(rowY.flatMap((y) => colX.map((x) => ({ x, y }))))
</script>

<svg
    xmlns="http://www.w3.org/2000/svg"
    width={width}
    height={height}
>
    <defs>
        <mask id="house-windows">
            <path d={housePath} fill="white" />
            {#each windows as w}
                <rect x={w.x} y={w.y} width={win} height={win} fill="black" />
            {/each}
        </mask>
    </defs>

    <path d={housePath} fill="white" mask="url(#house-windows)" />
</svg>