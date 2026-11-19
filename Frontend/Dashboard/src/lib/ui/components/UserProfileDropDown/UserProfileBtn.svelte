<script lang="ts">
    import type { LucideIcon } from '@lucide/svelte';

    let { icon: Icon, iconSize, text, handler }: { icon: LucideIcon; iconSize: number; text: string, handler: () => void } = $props();
</script>

<button class="flex gap-4 p-4 items-center border-t border-gray-200 cursor-pointer transition-colors duration-100 hover:bg-gray-100" onclick={handler}>
    <Icon size={iconSize} color="rgba(100,100,100,1)"></Icon>
    <p class="text-sm">{text}</p>
</button>