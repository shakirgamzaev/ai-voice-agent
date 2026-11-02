<script lang="ts" module>
    import type { LucideIcon } from "@lucide/svelte";

    export type SectionLinkProps = {
        icon: LucideIcon;
        text: string;
        isSelected?: boolean;
    };
</script>

<script lang="ts">
    import SectionLink from "#lib/ui/CustomButtons/SectionLink.svelte";

    type Props = {
        title: string;
        links: SectionLinkProps[];
    };

    let { title, links }: Props = $props();
</script>

<div class="grid grid-cols-[1fr] gap-y-2">
    <h2 class="text-[0.9rem] text-[#939393] pl-3">{title}</h2>

    {#each links as link (link.text)}
        <SectionLink icon={link.icon} iconSize={18} gap={0.8} text={link.text} isSelected={link.isSelected}></SectionLink>
    {/each}
</div>
