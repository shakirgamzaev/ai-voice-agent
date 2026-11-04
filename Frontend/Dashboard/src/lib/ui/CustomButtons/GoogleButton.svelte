<script lang="ts">
    import googleLogo from "#lib/assets/google-logo.jpg";

    let {logoSize, text}: {logoSize: number, text: string} = $props()
</script>


<button class="flex justify-center gap-3 items-center p-2 rounded-md border border-[#808080] shadow-[2px_2px_7px_rgba(0,0,0,0.1)] cursor-pointer active:opacity-55">
    <img src={googleLogo} alt="" width={logoSize} height={logoSize}>
    <p class="text-[0.94rem]">{text}</p>
</button>