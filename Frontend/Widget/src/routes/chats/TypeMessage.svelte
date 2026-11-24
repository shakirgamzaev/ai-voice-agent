<script lang="ts">
	import { Send } from "@lucide/svelte";


</script>

<div>
    <div class="h-[2px] bg-[#dbdbdb]"></div>
    <div class="flex items-start min-h-[10rem] gap-8 p-4">
    <input type="text" class="grow p-2" placeholder="Type your message...">
    <button>
        <div class="rounded-xl bg-blue-100 p-2.5 bg-blue-700">
            <Send color="white" size={20}/>
        </div>
    </button>
</div>
</div>

