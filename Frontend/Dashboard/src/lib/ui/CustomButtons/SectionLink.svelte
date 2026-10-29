<script lang="ts">
    import type { LucideIcon } from "@lucide/svelte";

    type Props = {
        icon: LucideIcon
        isSelected?: boolean
        iconSize: number
        gap: number
        text: string
    };
    let { icon: Icon, isSelected = false, iconSize, gap, text}: Props = $props();
</script>

<button
    class={[
        "flex w-full p-2 justify-start items-center cursor-pointer rounded-xl",
        isSelected && "bg-linear-to-b from-[#508dff] to-[#2563eb]",
    ]}
    style:gap="{gap}rem"
>
    <Icon size={iconSize} color={isSelected ? "white" : "black"}></Icon>
    <p class={`${isSelected ? "text-white" : "text-black"} text-[15px]`}>{text}</p>
</button>