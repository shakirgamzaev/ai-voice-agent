<script lang="ts">
	import NavButton from "#lib/uiComponents/NavButton.svelte";


</script>

<main>
    <header class="flex flex-col items-start bg-linear-to-b from-[#508dff] to-[#2563eb] p-4 py-7 text-white gap-4">
        <h1 class="text-4xl">Hi there!</h1>
        <h3 class="">How can we help you today?</h3>
    </header>
    <section class="grid grid-cols-[1fr] p-4">
        <NavButton url="/chats"></NavButton>
    </section>
</main>
