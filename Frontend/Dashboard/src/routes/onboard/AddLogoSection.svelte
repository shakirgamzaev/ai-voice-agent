<script lang="ts">
	import { Upload } from "@lucide/svelte";
	import UploadButton from "./components/UploadButton.svelte";

    function uploadOrgImage() {

    }

</script>


<div class="grid grid-cols-[80px_1fr] grid-rows-[auto_auto] gap-y-3 gap-x-5">
    <p class="col-span-2">Logo</p>
    <div class=" bg-[#f4f4f4] rounded-md shadow-[inset_-0px_-0px_4px_rgba(0,0,0,0.1)] w-full aspect-square flex items-center justify-center">
        <Upload size={18} color="rgba(130,130,130,1)"></Upload>
    </div>
    <div class="flex flex-col items-start self-center gap-1">
        <UploadButton onUpload={uploadOrgImage}></UploadButton>
        <p>Recommended size: 1:1, max 5MB</p>
    </div>
</div>