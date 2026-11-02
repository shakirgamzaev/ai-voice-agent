<script lang="ts">
    import { Inbox, LibraryBig, ShieldCheck, Palette, Blocks, CreditCard } from "@lucide/svelte";
	import OrgNameDropDown from "./OrgNameDropDown.svelte";
    import LeftSideSection, { type SectionLinkProps } from "./LeftSideSection.svelte";

    let {children} = $props()

    const customerSupportLinks: SectionLinkProps[] = [
        { icon: Inbox, text: "Conversations", isSelected: true },
        { icon: LibraryBig, text: "Knowledge Base" }
    ];

    const configurationLinks: SectionLinkProps[] = [
        { icon: Palette, text: "Widget Customization" },
        { icon: Blocks, text: "Integrations" },
        { icon: ShieldCheck, text: "Voice Assistant"}
    ];
    const accountLinks: SectionLinkProps[] = [
        {icon: CreditCard, text: "Plans & Billing"}
    ]

</script>

<main class="grid grid-cols-[20rem_1fr] h-dvh">
    <!--Left section, (wraps all dashboard routes)-->
    <div class="flex flex-col p-2 gap-8">
        <OrgNameDropDown></OrgNameDropDown>

        <LeftSideSection title="Customer support" links={customerSupportLinks}></LeftSideSection>

        <LeftSideSection title="Configuration" links={configurationLinks}></LeftSideSection>

        <LeftSideSection title="Account" links={accountLinks}></LeftSideSection>
    </div>


    <!-- Right section where each custom route is displayed -->
    <div class="">
        {@render children()}
    </div>
</main>