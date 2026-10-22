<script lang="ts">
    let { text }: {text: string} = $props()
</script>

<button onclick={() => {console.log(`${text} clicked`);}} class="bg-black p-3 w-full max-w-[25rem] text-white rounded-2xl cursor-pointer active:opacity-75">
    {text}
</button>