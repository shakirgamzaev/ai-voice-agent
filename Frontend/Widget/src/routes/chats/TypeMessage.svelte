<script lang="ts">
	import { Send } from '@lucide/svelte';
</script>

<div>
	<div class="h-[2px] bg-[#dbdbdb]"></div>
	<div class="flex min-h-[10rem] items-start gap-8 p-4">
		<input type="text" class="grow p-2" placeholder="Type your message..." />
		<button>
			<div class="rounded-xl bg-blue-100 bg-blue-700 p-2.5">
				<Send color="white" size={20} />
			</div>
		</button>
	</div>
</div>
