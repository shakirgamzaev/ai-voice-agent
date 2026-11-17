<script lang="ts">
    let { onUpload }: { onUpload: () => void } = $props();
</script>

<button type="button" class="p-1 px-3 border border-[#0000002a] rounded-md text-gray-500 font-medium cursor-pointer active:bg-gray-100" onclick={() => onUpload()}>
    <p>Upload</p>
</button>
