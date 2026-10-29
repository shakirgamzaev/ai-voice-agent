<script lang="ts">
    import OrgHomeIcon from "#lib/ui/CustomButtons/OrgHomeIcon.svelte";
    import { ChevronDown } from "@lucide/svelte";

</script>

<div class="flex justify-between gap-2 items-center p-1">
    <div class="flex justify-start gap-2 items-center">
        <OrgHomeIcon iconWidth={9} iconHeight={15} padding={6}></OrgHomeIcon>
        <p class="text-[16px]">Acme Inc.</p>
    </div>
    <ChevronDown size={20}></ChevronDown>
</div>