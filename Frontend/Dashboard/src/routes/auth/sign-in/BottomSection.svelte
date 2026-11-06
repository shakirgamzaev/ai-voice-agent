<script lang="ts">
	import { resolve } from '$app/paths';
</script>

<div class="flex justify-between">
    <div class="flex gap-3 items-center">
        <input type="checkbox" class="w-4 h-4"/>
        <p>Remember me</p>
    </div>
	<a href={resolve('/auth/sign-in')}>Forgot Password?</a>
</div>
