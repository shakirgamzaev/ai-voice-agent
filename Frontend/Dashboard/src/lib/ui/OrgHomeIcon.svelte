<script lang="ts">
    import OrgHome from "./svgIcons/orgHome.svelte";

    // Icon dimensions and per-side padding, all in px.
    // The box is a square whose side = tallest icon dimension + 2*padding.
    let {
        iconWidth = 12,
        iconHeight = 17,
        padding = 6
    }: { iconWidth?: number; iconHeight?: number; padding?: number } = $props();

    const side = $derived(Math.max(iconWidth, iconHeight) + padding * 2);
</script>

<div
    class="grid place-items-center bg-[#7521f4] rounded-md"
    style:width="{side}px"
    style:height="{side}px"
>
    <OrgHome width={iconWidth} height={iconHeight}></OrgHome>
</div>