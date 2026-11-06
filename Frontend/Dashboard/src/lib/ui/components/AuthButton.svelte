<script lang="ts">
	let { text, authHandler, bgColor }: { text: string; authHandler: () => void; bgColor: string } =
		$props();
</script>

<button
	onclick={authHandler}
	style:background-color={bgColor}
	class="w-full cursor-pointer rounded-md p-3 text-white active:opacity-75"
>
	{text}
</button>
