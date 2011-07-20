<%namespace name="tw" module="tw2.core.mako_util"/>
<div>
	% for jsc, l in w._js_calls:
	<script type="text/javascript">
		${jsc}
	</script>
	% endfor
</div>
