<script lang="ts">
    let { isDisabled, createOrgHandler }: {isDisabled: boolean, createOrgHandler: () => void} = $props()
</script>

<button 
    type="button" 
    class="bg-black self-end text-white p-1.5 rounded-md px-4 mt-4 text-[0.9rem] enabled:cursor-pointer enabled:active:bg-gray-700 disabled:bg-gray-300 disabled:text-gray-500 disabled:cursor-not-allowed" disabled={isDisabled}
    onclick={createOrgHandler}
    >
    Create Organization
</button>
