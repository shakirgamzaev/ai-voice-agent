<script lang="ts">
    let { label, placeholder, value = $bindable('') }: {
        label: string;
        placeholder: string;
        value?: string;
    } = $props();
    const inputId = $props.id();
</script>

<div class="flex w-full flex-col items-start gap-2">
    <label for={inputId}>{label}</label>
    <input
        type="text"
        id={inputId}
        {placeholder}
        bind:value
        class="w-full rounded-md border border-gray-300 p-2 shadow-[0_0_2px_rgba(156,163,175,0.25)]  focus:border-gray-400 focus:shadow-[0_0_5px_rgba(107,114,128,0.8)] focus:outline-hidden"
    />
</div>
