import { QuartzComponentConstructor } from "./types"
import { FullSlug, resolveRelative } from "../util/path"

export default (() =>
  ({ fileData }) => (
    <a
      class="control-map-link"
      data-router-ignore="true"
      href={resolveRelative(fileData.slug!, "control-map/index" as FullSlug)}
    >
      Repository Control Map ↗
    </a>
  )) satisfies QuartzComponentConstructor
