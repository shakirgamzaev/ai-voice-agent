<script lang="ts">
    let {text, inputFieldType}: {text:string, inputFieldType: string} = $props()
</script>

<div class="flex flex-col items-start w-full gap-1.5">
    <p>{text}</p>
    <input type={inputFieldType} class="border rounded-md p-1 w-full py-2">
</div>