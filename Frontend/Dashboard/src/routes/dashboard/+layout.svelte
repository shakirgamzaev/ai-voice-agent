<script lang="ts">
    import { Inbox, LibraryBig } from "@lucide/svelte";
    import SectionLink from "#lib/ui/CustomButtons/SectionLink.svelte";
	import OrgNameDropDown from "./OrgNameDropDown.svelte";

    let {children} = $props()
</script>

<main class="grid grid-cols-[20rem_1fr] h-dvh">
    <!--Left section, (wraps all dashboard routes)-->
    <div class="flex flex-col p-2 gap-8">
        <OrgNameDropDown></OrgNameDropDown>

        <!--Customer support section -->
        <div class="grid grid-cols-[1fr] gap-y-2">
            <h2 class="text-[0.9rem] text-[#939393] pl-3">Customer support</h2>

            <SectionLink icon={Inbox} iconSize={18} gap={0.8} text="Conversations" isSelected={true}></SectionLink>

            <SectionLink icon={LibraryBig} iconSize={18} gap={0.8} text="Knowledge Base"></SectionLink>
        </div>

        <!--Configuration section-->
        <div class="grid grid-cols-[1fr] gap-y-2">
            <h2 class="text-[0.9rem] text-[#939393] pl-3">Configuration</h2>

            <SectionLink icon={Inbox} iconSize={18} gap={0.8} text="Widget Customization"></SectionLink>

            <SectionLink icon={LibraryBig} iconSize={18} gap={0.8} text="Knowledge Base"></SectionLink>
        </div>
    </div>


    <!-- Right section where each custom route is displayed -->
    <div class="">
        {@render children()}
    </div>
</main>