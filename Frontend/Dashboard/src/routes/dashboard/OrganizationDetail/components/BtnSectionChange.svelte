<script lang="ts">
    import type { LucideIcon } from '@lucide/svelte';

    let {
        icon: Icon,
        text,
        iconSize,
        isSelected,
        onclick
    }: {
        icon: LucideIcon;
        text: string;
        iconSize: number;
        isSelected: boolean;
        onclick: () => void;
    } = $props();
</script>


<button class={["flex items-center gap-2 p-2 rounded-md cursor-pointer", isSelected && "bg-gray-200"]} {onclick}>
    <Icon size={iconSize}></Icon>
    <p class="text-[0.9rem]">{text}</p>
</button>