<script lang="ts">
    import {getInitials} from "#lib/utils/getNameInitials.ts"

    // size is the circle's diameter in px; the initials scale with it.
    let { userName, size }: {userName: string, size: number} = $props()
</script>

<span class="flex justify-center items-center  rounded-full bg-red-700 text-white"
    style:width="{size}px"
    style:height="{size}px"
    style:font-size="{size * 0.4}px">
    {getInitials(userName)}
</span>
