<script lang="ts">
	let {
		size = 24,
		angle = 270,
		strokeColor = 'currentColor'
	}: {
		size?: number;
		/** Clockwise arc span in degrees, greater than 0 and less than 360. */
		angle?: number;
		strokeColor?: string;
	} = $props();

	const center = $derived(size / 2);
	const strokeWidth = $derived(size / 10);
	// Inset the centerline so the entire stroke fits inside the SVG.
	const radius = $derived((size - strokeWidth) / 2);

	// The leftmost point of the circle is at 180 degrees.
	const startX = $derived(center - radius);
	const startY = $derived(center);
	const endAngle = $derived(((180 + angle) * Math.PI) / 180);
	const endX = $derived(center + radius * Math.cos(endAngle));
	const endY = $derived(center + radius * Math.sin(endAngle));
	const largeArcFlag = $derived(angle > 180 ? 1 : 0);
</script>

	<svg
		width={size}
		height={size}
		viewBox={`0 0 ${size} ${size}`}
		xmlns="http://www.w3.org/2000/svg"
		class="animate-spin motion-reduce:animate-none"
		role="img"
		aria-label="Loading"
	>
		<path
			d={`M ${startX} ${startY} A ${radius} ${radius} 0 ${largeArcFlag} 1 ${endX} ${endY}`}
			fill="none"
			stroke={strokeColor}
			stroke-width={strokeWidth}
			stroke-linecap="round"
		/>
	</svg>

