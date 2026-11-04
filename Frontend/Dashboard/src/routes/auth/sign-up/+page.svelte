<script lang="ts">
    import AuthButton from "#lib/ui/CustomButtons/AuthButton.svelte";
	import GoogleButton from "#lib/ui/CustomButtons/GoogleButton.svelte";
	import TextField from "#lib/ui/CustomButtons/TextField.svelte";
</script>

<main class="flex items-center justify-end p-8 ">
    <div class="flex flex-col max-w-[40rem] p-6 bg-white grow gap-5 rounded-2xl shadow-[3px_3px_8px_4px_rgba(0,0,0,0.14)]">
        <div class="grid grid-cols-[1fr] justify-items-start">
            <h1 class="text-4xl">Welcome Back</h1>
             <h3 class="text-[#5f5f5f]">Sign in to your workspace</h3>
        </div>
        <div class="grid grid-cols-[1fr] gap-y-5">
            <GoogleButton logoSize={30} text="Continue with Google"></GoogleButton>
            <div class="flex items-center">
                <div class="h-[1px] grow bg-[#5d5d5d]"></div>
                <p class="px-3">or sign in with email</p>
                <div class="h-[1px] grow bg-[#5d5d5d]"></div>
            </div>
        </div>
        <div class="grid grid-cols-[1fr] gap-y-5">
            <TextField 
                text="Email" 
                inputFieldType="email">
            </TextField>
            <TextField 
            text="Password"
            inputFieldType="password">
            </TextField>
        </div>
        
    </div>
</main>