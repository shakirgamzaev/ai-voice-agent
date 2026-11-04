<script lang="ts">
	import OrgHomeIcon from '#lib/ui/components/OrgHomeIcon.svelte';
	import { ChevronDown } from '@lucide/svelte';
</script>

<div class="flex items-center justify-between gap-2 p-1">
	<div class="flex items-center justify-start gap-2">
		<OrgHomeIcon iconWidth={9} iconHeight={15} padding={6}></OrgHomeIcon>
		<p class="text-[16px]">Acme Inc.</p>
	</div>
	<ChevronDown size={20}></ChevronDown>
</div>
